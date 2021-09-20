.. _quick start to quick start:

Quick Start
===========

After you have :ref:`installed Nextflow <install to install>` you can
download the latest version of MIAAIM directly from GitHub by typing::

  git clone https://github.com/JoshuaHess12/miaaim.git  # clone MIAAIM repository

If you have already cloned MIAAIM from GitHub, ensure that you have
the latest version by entering the directory where you are storing MIAAIM and typing
:code:`git pull`

MIAAIM currently contains one prototype use case with pre-configured parameters for
multi-modal image registration.

prototype-001
^^^^^^^^^^^^^

prototype-001 is a coupled MALDI-TOF mass spectrometry imaging (MSI) and H&E data
set from a prostate tumor biopsy. In this example, the MSI dataset is
considered the "moving" image, and the H&E data set is the "fixed" image.
Run through this example workflow by following the following steps.

.. warning::
    Executing all steps for prototype-001 will require you to have ~5GB of free
    space on your computer.

Download Data
-------------

1. To download the prototype folder and unzip its contents to your current working
directory. You should be able to inspect the contents of the :code:`input` folder
to confirm that the download was successful.

::

  nextflow run JoshuaHess12/miaaim/prototype.nf --proto prototype-001 --out .

.. note::
    If you are using a larger workstation consider checking out the
    :ref:`Configuration <Configs to Configs>` to allocate more
    resources for your computations. With the preset files, you can
    add :code:`-profile medium_multi` to the following steps to use more computing
    resources.

Image Preprocessing
-------------------

2. The first step of the pipeline is processing each image so that they can
be aligned later in the pipeline. To process the images for prototype-001,
type the following command:

::

  nextflow run miaaim --in prototype-001 --startAt hdiprep --stopAt hdiprep
  --fixedImage "fixed" --movingImage "moving" --fixedPars "fixed.yaml"
  --movingPars "moving.yaml"


Image Registration
------------------

3. After processing each of the images, type the following command to register
the moving image to the fixed image:

::

  nextflow run miaaim --in prototype-001 --fixedImage "fixed" --movingImage "moving"
  --fixedPars "fixed.yaml" --movingPars "moving.yaml"
  --elastix-pars "--p affine_short.txt nonlinear_short.txt"
  --transformix-pars "--tps TransformParameters.0.txt TransformParameters.1.txt --pad 20 20 --target_size 2472 1572"
  --transformix false
  -resume

4. After registering the images, apply the transformation matrices to each channel
in the moving image by executing the following command:

::

  nextflow run miaaim --in prototype-001 --fixedImage "fixed" --movingImage "moving"
  --fixedPars "fixed.yaml" --movingPars "moving.yaml"
  --elastix-pars "--p affine_short.txt nonlinear_short.txt"
  --transformix-pars "--tps TransformParameters.0.txt TransformParameters.1.txt --pad 20 20 --target_size 2472 1572"
  --transformix true
  -resume
