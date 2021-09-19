Contributing
============


Adding Imaging Modalities
^^^^^^^^^^^^^^^^^^^^^^^^^
Imaging modalities can be added to MIAAIM by modifying the
`hdi-utils <https://github.com/JoshuaHess12/hdi-utils>`_ utility
toolbox, which is used throughout each workflow in MIAAIM. Directions for
adding new imaging modalities to the pipeline by modifying the hdi-utils
repository are outlined below.

Importing New Modalities / Adding File Formats
----------------------------------------------
Because many imaging modalities store data for a single experiment in more than
one file, all imaging modalities in MIAAIM are assumed to be contained within
a folder that indicates the sample identity (although, images created with a
single file can be read without the folder structure.). To create a new data
modality for MIAAIM, all that should be needed is a function within the
hdi-utils module to read the data. If you would like to contribute, please
:ref:`contact us <Contact Information to contact>`.
