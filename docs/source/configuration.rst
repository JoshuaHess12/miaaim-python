Configuration
=============
MIAAIM utilizes software containers for individual processes within its Nextflow
workflow. Configuration settings for each individual process can be set using
the :code:`nextflow.config` file in the main MIAAIM repository. Passing
configuration settings to Nextflow upon running your analysis is done by specifying
your

Docker/Singularity Containers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Resource Allocation
^^^^^^^^^^^^^^^^^^^
Configuring resource allocation within each Docker image can be achieved
by modifying or adding configuration files (in :code:`config` folder of MIAAIM repo)
and linking those with the :code:`nextflow.config` file in the main repository.

::

  miaaim                    # main repository
  ├── LICENSE
  ├── README.md
  ├── miaam.nf
  ├── nextflow.config       # Nextflow configuration in main repo
  ├── workflows
  ├── docs
  ├── config                # config folder with custom configurations
  │   └──medium.config      # example configuration file that can be modified or added

Each of your processes within the MIAAIM pipeline can have resources allocated to its
respective container image.

Memory
------
Memory allocation can be set for individual processes using the :code:`memory`
indicator. For example, this is the medium.config file for jobs that require medium sized
memory allocation. This file sets a time limit on each process, and allocates
40GB of memory to each.

::

  process {
    withName:hdiprep   {
      time   = '6h'
      memory = '40G'
    }
    withName:elastix   {
      time   = '6h'
      memory = '40G'
    }
    withName:transformix   {
      time   = '6h'
      memory = '40G'
    }
  }

CPU
---
CPU allocation can be set for individual processes using the :code:`cpu`
indicator. For example, this is the multi.config file for jobs that require multiple
cpus. This file sets a time limit on each process, and allocates
30 cpus to each.

::

  process {
    withName:hdiprep   {
      time   = '6h'
      cpus = 30
    }
    withName:elastix   {
      time   = '6h'
      cpus = 30
    }
    withName:transformix   {
      time   = '6h'
      cpus = 30
    }
  }



Preset Resource Allocation Options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
MIAAIM provides sensible defaults for job scheduling. We separated cpu usage from
memory allocation to provide a mix of resource usage options. Feel free to add or modify
our configuration settings within your project!

.. list-table:: Preset Resource Allocation Options in MIAAIM
   :widths: 33 33 33
   :header-rows: 1

   * - Flag
     - Memory
     - CPUs
   * - standard
     -
     -
   * - medium
     - 40GB
     -
   * - multi
     -
     - 30
   * - medium_multi
     - 40GB
     - 30
