API Guide
=========
Here we outline the modules, classes, and key functions to use in the MIAAIM
workflow in Python.

Image Preparation (HDIprep)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

hdi_prep
--------

.. automodule:: hdiprep.HDIprep.hdi_prep
   :members:

utils
-----

.. automodule:: hdiprep.HDIprep.utils
   :members:


Image Registration (HDIreg)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

elastix
-------

.. automodule:: hdireg.HDIreg.elastix
   :members:

transformix
-----------

.. automodule:: hdireg.HDIreg.transformix
   :members:

utils
-----

.. automodule:: hdireg.HDIreg.utils
   :members:

Tissue State Modeling (PatchMAP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. currentmodule:: patchmap.patchmap_

.. autofunction:: compute_cobordism

.. autofunction:: embed_cobordism


Cross-System/Tissue Information Transfer (i-PatchMAP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: compute_i_patchmap_cobordism

.. autofunction:: i_patchmap
