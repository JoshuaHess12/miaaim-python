Folder Structure
================
Each workflow within MIAAIM produces output in a directory that
reflects the workflow name. For more complete background on workflows and
how to structure parameter files for each, check out the
:ref:`Workflows section <Workflows to Workflows>`.
Here is the current directory structure and optional outputs for each:

 ::

    imageID                         # image name
    ├── input                          # raw input
    │   ├── fixed                           # fixed image folder
    │   │   └── fixed.ext                       # fixed image with extension (ext)
    │   ├── moving                          # moving image folder
    │   │   └── moving.ext                      # moving image with extension (ext)
    │   ├── fixed-pars.yaml                 # fixed image processing parameters
    │   ├── moving-pars.yaml                # moving image processing parameters
    │   └── registration-pars.txt           # registration parameters
    ├── hdiprep                        # hdiprep workflow
    │   ├── fixed_processed.nii             # processed fixed image
    │   └── moving_processed.nii            # processed moving image
    ├── hdireg                         # hdireg workflow
    │   ├── elastix                         # registration
    │   │   ├── Iteration.txt                   # optimization log
    │   │   ├── TransformationParameters.txt    # spatial transformation parameters
    │   │   └── result.nii                      # single-channel export example
    │   └── transformix                     # FINAL RESULTS FOLDER
    │       ├── moving_result.ext               # exported results
    │       └── fixed.ext                       # fixed image (optional)
    └── docs                           # provenance module
        ├── miaaim-pars.yaml                # workflow parameters
        ├── hdiprep-fixed.log               # hdiprep fixed image log
        ├── hdiprep-fixed.sh                # hdiprep fixed image command
        ├── hdiprep-moving.log              # hdiprep moving image log
        ├── hdiprep-moving.sh               # hdiprep moving image command
        ├── hdireg-elastix.log              # hdireg elastix log
        ├── hdireg-elastix.sh               # hdireg elastix command
        ├── hdireg-transformix.log          # hdireg transformix log
        └── hdireg-transformix.sh           # hdireg transformix command

MIAAIM is developed to integrate assembled images in the level 2 format. Your
base folder, :code:`imageID` should contain your assembled image sample name.

.. note::
   All you need to supply for MIAAIM are the contents of the :code:`input` folder.
   MIAAIM will automatically create and populate all other folders in the above
   directory tree.

input
-----
All input files should be included in the :code:`input` folder. These include
the raw input images, parameters for preprocessing, and elastix
image registration parameters.

Because many imaging modalities store data for a single experiment in more than
one file, all imaging modalities in MIAAIM are assumed to be contained within
a folder that indicates the sample identity (although, images created with a
single file can be read without the folder structure).

An example of a typical :code:`input` folder structure with is shown below:

.. figure:: images/input-folder-example.png
   :width: 100%

Here, the fixed image is in the :code:`TIFF` format, and the moving image is
a mass spectrometry imaging data set stored in the :code:`imzML` format. The
processing steps for the moving and fixed image to pass to HDIprep
are stored in the :code:`YAML` files, and the registration parameters to feed
to HDIreg are stored in the :code:`registration-pars.txt` file.

hdiprep
-------
The :code:`hdiprep` folder will contain results for image preparation. These will
be image data sets, either compressed through the HDIprep compression workflow,
or preprocessed using histological image processing options.

An example of a typical :code:`hdiprep` folder structure with its output
is shown below:

.. figure:: images/hdiprep-folder-example.png
   :width: 100%

.. note::
   Processed data will contain original images' file names with the suffix
   :code:`_processed.nii` appended.

hdireg
-------
The :code:`hdireg` folder will contain results for image registration. The
HDIreg workflow can compose multiple image registration models, indicated by
separate parameter files.

An example of a typical :code:`hdireg` folder structure with its output
is shown below:

.. figure:: images/hdireg-folder-example.png
   :width: 100%

Here, there are two folders: :code:`elastix`, which stores the registration
logs and transformation matrices for the registration, and :code:`transformix`,
which stores the final result of the registration procedure after the transformation
matrix is applied to the full moving image.

The optimization log for the registration is stored in the
:code:`IterationInfo.0.txt` file. This was a single-resolution registration, so
there is only a single file. Additional logs would be indicated increasing numbers
at the end of the file name.

The transformation parameters are stored in the :code:`TransformationParameters.0.txt` file,
and these are the parameters that transform each channel in the moving image
when the :code:`transformix` flag is passed to the hdireg module
(see the :ref:`Parameter Reference <Parameter Reference to Parameter Reference>`)

An example of the registration results are stored in the :code:`result.0.nii`
file. This is the transformation matrix applied to the first channel of the
:code:`moving_processed.nii` image in the :code:`hdiprep` folder.

.. note::
   Chaining together registration parameters will be stored as separate
   transformation parameter files, indicated by the order which they were
   applied. For example, and affine registration followed by nonlinear registration
   would produce two parameter files, :code:`TransformationParameters.0.txt` and
   :code:`TransformationParameters.1.txt`. Both of these should be supplied as
   parameters to transformix when producing final results.

docs
-------
The commands and output logs for each workflow in MIAAIM is automatically
stored in the :code:`docs` folder. Here you will find each of the commands
run, and the final parameters for the complete nextflow application will be stored
in the :code:`miaaim-pars.yml` file.

An example of a typical :code:`docs` folder structure with its output
is shown below:

.. figure:: images/docs-folder-example.png
   :width: 100%
