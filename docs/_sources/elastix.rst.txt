Elastix Basics
==============
MIAAIM's core registration component utilizes the `elastix <https://elastix.lumc.nl>`_
image registration library. Elastix provides a multitude of similarity measures,
transformation models, optimizers, and interolators for image alignment.
For a complete list of these, see the elastix documentation, in particular the
`manual <https://github.com/SuperElastix/elastix/wiki/Documentation>`_. `Elastix's
model zoo <https://elastix.lumc.nl/modelzoo/>`_ also contains a number of
examples from the community that can get you started and acclamated to the way
that elastix implements user's parameters.

Registration Parameter Files (Elastix)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Input to elastix requires a text document parameter file (or multiple files) that indicates
the settings and algorithms to be used for image registration. Example parameter
files that would typically be used for MIAAIM registration are stored in the
`templates <https://github.com/JoshuaHess12/miaaim/tree/master/templates>`_
folder within the MIAAIM GitHub repository.

Included in the :code:`templates` folder are example parameter files for k-nearest neighbor
alpha-mutual information (KNN alpha-MI) based registration and single-channel
mutual information for histological stains.

.. tip::
  The :code:`templates` folder in MIAAIM is primarily based on settings that have
  been used in our laboratories. We find that changing parameters for the number of
  levels for multi-resolution hierarchical pyramids and optimization iterations
  make a difference in the outcome of registration. In the case of nonlinear
  registrations, the final spacing for the transformation grid parametrized by
  B-splines makes a big difference -- smaller values capture small-scale
  structure but risk warping the image unrealistically. These parameters are changed
  as follows::

    # Example parameters for elastix .txt file
    // Total number of resolutions
    (NumberOfResolutions 4)

    // Number of optimization iterations
    (MaximumNumberOfIterations 1000)

    // Nonlinear registration final grid spacing
    (FinalGridSpacingInVoxels 40)

Multi-channel Input
-------------------
Multi-channel image registration in MIAAIM is carried out using KNN alpha-MI
as a similarity measure. This measure extends to feature spaces (number of channels)
of potentially mis-matched dimensionalities. For example, we have used this measure
to align 3-, 4-, 5-channel compressed images with 3-channel H&E stains.

Using this measure in elastix is done by altering your registration type and
metric in the elastix parameter text file as follows::

  (Registration "MultiResolutionRegistrationWithFeatures")
  (Metric "KNNGraphAlphaMutualInformation")

For multi-channel input, elastix requires that the user export individual channels
of their image, and pass each of these as a command line argument. The HDIreg module
in MIAAIM does this automatically. In addition, elastix requires that your interpolator and
fixed/moving image pyramids match the number of channels in your image. For example,
the following snippet indicates the parameters used to align a 4-channel moving image
to a 3-channel fixed image::

  // Image interpolator -- matches moving image
  (Interpolator "BSplineInterpolator" "BSplineInterpolator" "BSplineInterpolator"
  "BSplineInterpolator")

  // Fixed image multi-resolution pyramid -- matches fixed image
  (FixedImagePyramid "FixedSmoothingImagePyramid" "FixedSmoothingImagePyramid"
  "FixedSmoothingImagePyramid")

  // Moving image multi-resolution pyramid -- matches moving image
  (MovingImagePyramid "MovingSmoothingImagePyramid" "MovingSmoothingImagePyramid"
   "MovingSmoothingImagePyramid" "MovingSmoothingImagePyramid")


.. warning::
  The current release of MIAAIM (0.0.1) doesn't automatically fill in the
  appropriate input for multi-channel registration. This is the focus of a future
  release! For now, you will need to adjust the parameter file according to the
  number of channels in your images.

Single-channel Input
--------------------
Single-channel registration in MIAAIM will be carried on grayscale images -- if
you attempt to use single-channel parameters on multi-channel images, only the
first channel will be used for registration.

Help the Registration with Manual Landmarks
-------------------------------------------

Outputs
-------
Elastix parameter files contain options to export intermediate files showing
registration optimization and a single-channel image that shows results for the
registration. These are indicated in the elastix parameter text file as follows::

  // Options for writing optimization results
  (WriteTransformParametersEachIteration "false")
  (WriteTransformParametersEachResolution "false")
  (WriteResultImageAfterEachResolution "false")

  // Write result image for visualizing results
  (WriteResultImage "true")

  // Return the image pixels as double type
  (ResultImagePixelType "double")

  // Leave the resulting image format as .nii since HDIprep exports .nii files!
  (ResultImageFormat "nii")

To visualize intermediate results for human-in-the-loop parameter tuning and
registration adjustment, we recommend that you export an image using the :code:`WriteResultImage`
option. This image will be a single-channel of your moving image.
You can overlay this image with your fixed image to get a sense of what the registration
results look like. Alternatively, you can proceed to transform your entire image stack
with transformix. This may take more time if you are registering large images.

.. note::
  HDIprep utilizes the NIfTI format for image preprocessing and compression. It is
  recommended to leave the resulting image format as :code:`nii` for visualizing
  results to keep export formats consistent.

Elastix will export parameter files for each transformation model that is included
in the registration process. These will be stored in files called
:code:`TransformParameters.txt`. Each of these files will be numbered according to
the order that they were carried out. For example, a single registration model will
export a file called :code:`TransformParameters.0.txt`, and any additional registrations
will be sequentially added.

.. note::
  Transform parameter files are the text files used during the transformix
  portion of the HDIreg module.

Applying Transformations (Transformix)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
After elastix has calculated the transformation parameters needed to align images,
MIAAIM applies the transformation to each channel of the moving image using
elastix's native transformix method. The HDIreg module performs the heavy lifting
for this -- all you need to do is indicate the resulting image type (file extension)
and the transform parameters that will be used. If padding or image resizing was
used for the HDIprep module, the HDIreg module can take this into account when
transforming the original multi-channel image stack.

.. tip::
  When running transformix in the HDIreg module, make sure the number of transform
  parameter files match the number of registration models that you used in elastix!
