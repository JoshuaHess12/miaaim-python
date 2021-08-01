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

1. prototype-001 is a coupled MALDI-TOF mass spectrometry imaging (MSI) and H&E data
set from a prostate tumor tissue bioppsy. Run through this example workflow by typing::

  nextflow run JoshuaHess12/miaaim/prototype.nf --proto prototype-001 --out .

To download the prototype folder and unzip its contents to your current working
directory. You should be able to inspect the contents of the :code:`input` folder
to confirm that the download was successful. Initiate the registration workflow
by typing::

  nextflow run JoshuaHess12/miaaim --in prototype-001 --out . --transformix

Results can be visualized using ImageJ/FIJI:
