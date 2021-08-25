.. _Pworkflows to Pworkflows:

Workflow Implementations in Python
==================================
MIAAIM's workflows can also be run in Python to allow for more user flexibility with
custom workflow creation. To install `MIAAIM in Python
<https://github.com/JoshuaHess12/miaaim-python>`_, follow these steps:

Image Preparation (HDIprep)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The HDIprep workflow can be used in Python, just as it can be used in the
command line interface. Commands are sequentially applied to images and
are specified by the user.

Steady-state UMAP compression
-----------------------------
Here, we will run through an example of using the HDIprep workflow in MIAAIM
to create steady-state UMAP embeddings of a high-dimensional image data set. We
will be using the mass spectrometry imaging data from prototype-001:

1. First import the necessary modules. We will also define a helper function
   to create plots after UMAP embedding.

.. code-block:: python3

   # import hdi utils module
   import hdiutils.HDIimport.hdi_reader as hdi_reader
   # import hdi_prep module
   from miaaim.hdiprep.HDIprep import hdi_prep
   # import external modules
   import matplotlib.pyplot as plt
   from sklearn.preprocessing import minmax_scale
   import matplotlib.patches as mpatches

   # create function for easy plotting
   def plot_rgb_2D(
                   embedding,
                   axs=(0,1),
                   cols=(0,1,2),
                   out_name=None
                   ):
       """
       helper function for plotting 2D scatter plots from dimension reduction method.

       axs: tuple of 2 integers indicating which axes to extract for plotting
       cols: tuple of 3 integers indicating which axes to use for RGB coloring
       out_name: name to export image as (if None, then no image exported)
       """

       # create rgb scale based off first 3 channel
       rgb=minmax_scale(embedding[:,cols])
       # extract the columns to plot
       to_plot=embedding[:, axs]

       # create manual legend items for plotting purposes
       red_patch = mpatches.Patch(color='red', label='UMAP 1')
       green_patch = mpatches.Patch(color='green', label='UMAP 2')
       blue_patch = mpatches.Patch(color='blue', label='UMAP 3')

       # scatter plot
       fig, ax = plt.subplots()
       plt.scatter(to_plot[:,0],to_plot[:,1],color=rgb,s=15,linewidths=0)
       fig.suptitle('Steady State UMAP Embedding', fontsize=12)
       plt.xlabel('UMAP {}'.format(str(axs[0]+1)), fontsize=12)
       plt.ylabel('UMAP {}'.format(str(axs[1]+1)), fontsize=12)
       plt.legend(handles=[red_patch,green_patch,blue_patch],title='Linear Scale')
       plt.savefig(out_name,dpi=400,pad_inches = 0.1,bbox_inches='tight')
       plt.close()

2. Next, we will import the data and run the steady-state UMAP embedding on the
prototype dataset.

.. code-block:: python3

   # read data with HDIutils
   mov_im = hdi_reader.HDIreader(
                       path_to_data=path_to_im,
                       path_to_markers=None,
                       flatten=True,
                       subsample=None,
                       mask=None,
                       save_mem=True
                       )
   # create data set using HDIprep module
   mov_dat = hdi_prep.IntraModalityDataset([mov_im])
   # apply steady state UMAP embedding
   mov_dat.RunOptimalUMAP(
                           dim_range=(1,11),
                           landmarks=3000,
                           export_diagnostics=True,
                           output_dir=out_path,
                           n_jobs=1
                           )

Since we chose to export diagnostic plots using :code:`export_diagnostics=True`,
we obtained a resulting image of the exponential fit to the fuzzy set cross entropy
that was used to compute the steady-state UMAP embedding:

.. image:: images/OptimalUMAP-prototype-001.jpeg

3. Now we can export a scatter plot of the 4-dimensional steady-state UMAP
   embedding in Euclidean space. Here the colors are RGB values created from the
   first 3 components of the embedding:

.. code-block:: python3

   # for plotting purposes, extract the key of the umap embedding
   key = list(mov_dat.umap_embeddings.keys())[0]
   # plot the embedding of the UMAP in Euclidean space
   embed = mov_dat.umap_embeddings[key]
   # export a plot of the results in Euclidean space
   plot_rgb_2D(embed.values, out_name="steady-state-UMAP-prototype-001.jpeg")

.. image:: images/steady-state-UMAP-prototype-001.jpeg

4. A final step to process prototype-001 is to reconstruct the original raster
   object using the coordinates of each pixel. Since the
   image was not a rectangular array, we will map it back to the spatial domain
   using the :code:`method="coordinate"` option for the :code:`SpatiallyMapUMAP` function.

.. tip::
   Running steady-state image processing on data that is stored an array
   format follows the same process here, except the spatial mapping with
   :code:`SpatiallyMapUMAP` uses the :code:`method="rectangular"` option.

.. code-block:: python3

   # reconstruct spatial image from UMAP embedding
   mov_dat.SpatiallyMapUMAP(method="coordinate")
   # extract processed image
   proc_im = mov_dat.set_dict[key].hdi.data.processed_image
   #plot the image using matplotlib (only the first 3 channels using RGB scale)
   plt.imshow(proc_im[:,:,(0,1,2)])

.. image:: images/steady-state-UMAP-prototype-001-spatial.jpeg

5. The last step is to export the image for subsequent registration to its H&E
   stained counterpart. Here we export the image with padding and image resizing
   and view the results:

.. code-block:: python3

   # export the processed image to the nifti format for image registration
   # here we pad the image and resize it using bilinear interpolation for
   # registration with the corresponding H&E image.
   mov_dat.ExportNifti1(
                       output_dir="/Users/joshuahess/Desktop/",
                       padding="(20,20)",
                       target_size="(2472,1572)"
                       )
   # load the exported image and view
   exported = hdi_reader.HDIreader(
                       path_to_data="/Users/joshuahess/Desktop/prostate_processed.nii",
                       path_to_markers=None,
                       flatten=False,
                       subsample=None,
                       mask=None,
                       save_mem=False
                       )
   # plot the exported image
   plt.imshow(exported.hdi.data.image[:,:,(0,1,2)])

.. image:: images/steady-state-UMAP-prototype-001-spatial-resize.jpeg

Histological Image Processing
-----------------------------
Here we will demonstrate an example of running histology image processing on the
H&E imaging modality. We will be using the prostate H&E imaging data from
prototype-001 in the MIAAIM software.

1. First import the necessary modules.

.. code-block:: python3

   # import hdi utils module
   import hdiutils.HDIimport.hdi_reader as hdi_reader
   # import hdi_prep module
   from miaaim.hdiprep.HDIprep import hdi_prep
   # import external modules
   import matplotlib.pyplot as plt
   import os

2. Now we will set the path to our imaging data and the output folders, and we will
read in the imaging data set using the :code:`HDIreader` class from the :code:`hdi-utils`
python package. We will then create a dataset using the :code:`HDIprep` module
imported above.

.. code-block:: python3

   # set the path to the imaging data
   path_to_im = "/Users/joshuahess/Desktop/prototype-001/input/fixed"
   # set the path to the output directory
   out_path = "/Users/joshuahess/Desktop/prototype-001/notebook-output"

   # read data with HDIutils
   fix_im = hdi_reader.HDIreader(
                    path_to_data=path_to_im,
                    path_to_markers=None,
                    flatten=False,
                    subsample=None,
                    mask=True,
                    save_mem=False
                    )
   # create data set using HDIprep module
   fix_dat = hdi_prep.IntraModalityDataset([fix_im])
   # for plotting purposes, extract the key of the data set
   key = list(fix_dat.set_dict.keys())[0]

3. Now use the :code:`IntramodalityDataset` class to run sequential morphological
operations. Here we will show the input H&E image along with the manually drawn
mask that we will use to help our image processing pipeline.

.. note::

   All data are stored in the :code:`IntramodalityDataset` as dictionary objects,
   kept under their filename as the key.

.. code-block:: python3

   # plot the histology image
   plt.imshow(fix_dat.set_dict[key].hdi.data.image)

.. image:: images/histology-prototype-001-1-raw.jpeg

.. code-block:: python3

   # plot the input manually drawn mask in ImageJ
   plt.imshow(fix_dat.set_dict[key].hdi.data.mask.toarray(),cmap='gray')

.. image:: images/histology-prototype-001-1-mask.jpeg

4. Next, we will convert the image to grayscale (carried out automatically in
the :code:`MedianFilter` function) and will use a median filter to remove salt and
pepper noise in the image prior to the thresholding process.

.. code-block:: python3

   # apply sequential processing steps
   # remove salt and pepper noise
   fix_dat.MedianFilter(filter_size=25,parallel=False)
   # extract the procesed image to show
   plt.imshow(fix_dat.set_dict[key].hdi.data.processed_image,cmap='gray')

.. image:: images/histology-prototype-001-1-med1.jpeg

5. After filtering, we will use the :code:`otsu` automatic thresholding method to convert
the grayscale image into a binary mask separating foreground from background.

.. code-block:: python3

   # create mask with thresholding
   fix_dat.Threshold(type='otsu')
   # extract the procesed image to show
   plt.imshow(fix_dat.set_dict[key].hdi.data.processed_image.toarray(),cmap='gray')

6. After thresholding, we will perform a series of morphological operations on the
mask to smooth edges, fill holes, and connect regions in the mask that should
represent the foreground (where the tissue is).

.. code-block:: python3

   # morphological opening
   fix_dat.Open(disk_size=20,parallel=False)
   # extract the procesed image to show
   plt.imshow(fix_dat.set_dict[key].hdi.data.processed_image.toarray(),cmap='gray')

.. image:: images/histology-prototype-001-1-open1.jpeg

.. code-block:: python3

   # morphological closing
   fix_dat.Close(disk_size=40,parallel=False)
   # extract the procesed image to show
   plt.imshow(fix_dat.set_dict[key].hdi.data.processed_image.toarray(),cmap='gray')

.. image:: images/histology-prototype-001-1-close1.jpeg

.. code-block:: python3

   # morphological fill
   fix_dat.Fill()
   # extract the procesed image to show
   plt.imshow(fix_dat.set_dict[key].hdi.data.processed_image.toarray(),cmap='gray')

.. image:: images/histology-prototype-001-1-fill1.jpeg

.. code-block:: python3

   # morphological opening
   fix_dat.Open(disk_size=15,parallel=False)
   # extract the processed image to show
   plt.imshow(fix_dat.set_dict[key].hdi.data.processed_image.toarray(),cmap='gray')

.. image:: images/histology-prototype-001-1-open2.jpeg

.. code-block:: python3

   # apply the manual input mask (will act on the previous masks)
   fix_dat.ApplyManualMask()
   # extract the processed image to show
   plt.imshow(fix_dat.set_dict[key].hdi.data.processed_image.toarray(),cmap='gray')

.. image:: images/histology-prototype-001-1-manualmask.jpeg

.. code-block:: python3

   # extract bounding box in the image for constant padding
   fix_dat.NonzeroBox()
   # extract the processed image to show
   plt.imshow(fix_dat.set_dict[key].hdi.data.processed_image.toarray(),cmap='gray')

.. image:: images/histology-prototype-001-1-boxed.jpeg

.. code-block:: python3

   # apply the final mask after all operations
   fix_dat.ApplyMask()
   # extract the processed image to show
   plt.imshow(fix_dat.set_dict[key].hdi.data.processed_image)

.. image:: images/histology-prototype-001-1-final.jpeg

7. We will now add padding to the edges of the image to register this image
to our mass spectrometry imaging data set. We recommend being a little generous
with how much padding you add -- leaving too little room on the edges of your
image may make the registration optimization more difficult.

We will export the image with padding and read it back into our session to
view the results:

.. code-block:: python3

   # export the processed image to the nifti format for image registration
   # here we pad the image for registration with the corresponding MSI
   # compressed image.
   fix_dat.ExportNifti1(
                       output_dir=out_path,
                       padding="(150,150)",
                       target_size=None
                       )

   # load the exported image and view
   exported = hdi_reader.HDIreader(
                       path_to_data=os.path.join(out_path,"fixed_processed.nii"),
                       path_to_markers=None,
                       flatten=False,
                       subsample=None,
                       mask=None,
                       save_mem=False
                       )
   # plot the exported image
   plt.imshow(exported.hdi.data.image)

.. image:: images/histology-prototype-001-1-padded-final.jpeg

Image Registration (HDIreg)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tissue State Modeling (PatchMAP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cross-System/Tissue Information Transfer (i-PatchMAP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
