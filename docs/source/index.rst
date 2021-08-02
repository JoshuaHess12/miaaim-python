.. miaaim documentation master file, created by
   sphinx-quickstart on Wed May  5 10:42:56 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


MIAAIM: multi-modal image alignment and analysis by information manifolds
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: twocol

   .. container:: leftside

      .. figure:: images/Figure1-5.jpg
         :width: 90%

   .. container:: rightside

      MIAAIM is a software to align and analyze multiple-omics tissue imaging data.
      The workflow includes high-dimensional image compression and preprocessing,
      image registration,
      tissue state modelling, and domain transfer.

      MIAAIM was developed by
      `Joshua Hess <https://github.com/JoshuaHess12>`_ at
      the `Vaccine and Immunotherapy Center at MHG <http://advancingcures.org>`_
      in the labs of `Dr. Ruxandra Sîrbulescu <http://advancingcures.org/sirbulescu-lab/>`_
      and `Dr. Patrick Reeves <http://advancingcures.org/reeves-lab/>`_.
      It is written in `Nextflow <https://www.nextflow.io>`_ with containerized
      workflows to enable reproducible
      image data integration across computing architectures.

      Before using this software, please read the relevant background for each
      workflow in the pipeline in the :ref:`Workflows <Workflows to Workflows>` section.
      For a complete description of the project, check our preprint on xxx.

.. note::
   MIAAIM is under active development! To update your current version, pull the
   latest release from GitHub with :code:`nextflow pull JoshuaHess12/miaaim`.
   If you pull a new version, please visit for the latest usage instructions for
   new workflows! We will try to make all updated versions backwards compatible
   with previous versions. If you are having trouble implementing a
   pipeline that you are used to after updating your MIAAIM version,
   feel free to :ref:`contact <Contact Information to contact>`
   us so we can help.

.. toctree::
   :maxdepth: 3
   :caption: Nextflow User Guide / Tutorials

   installation
   quick_start
   directory
   workflows
   parameters
   tutorials
   configuration
   executors
   provenance
   contributing

.. toctree::
   :maxdepth: 2
   :caption: MIAAIM in Python

   python
   python-workflows
   api

.. toctree::
   :maxdepth: 2
   :caption: Background on MIAAIM

   background
   elastix

.. toctree::
   :maxdepth: 2
   :caption: Roadmap

   roadmap

.. toctree::
   :maxdepth: 2
   :caption: Contributing

   contributing

.. toctree::
   :maxdepth: 2
   :caption: FAQs

   faqs

.. toctree::
   :maxdepth: 2
   :caption: Contact

   contact

.. toctree::
   :maxdepth: 2
   :caption: Funding

   funding

.. toctree::
   :maxdepth: 2
   :caption: License

   license

.. toctree::
   :maxdepth: 2
   :caption: Acknowledgements

   acknowledgements


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
