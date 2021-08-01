Executors
=========

Nextflow makes it convenient to provision the necessary resources to use for
large computations and/or computations that need to be run on specific excecution
systems. These systems include LSF and SLURM workload managers, Amazon Web Services
(AWS), and Google Cloud.

LSF (e.g. ErisOne MGH Computing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When submitting your job to an LSF scheduler, Nextflow will automatically
submit each process (workflow) as a separate job using :code:`bsub`, so your
jobs will run in parallel.

SLURM (e.g 02 HMS Computing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

AWS
^^^

Google Cloud
^^^^^^^^^^^^

Presets for Various Executors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
MIAAIM provides sensible defaults for submitting jobs on various execution systems.
Feel free to add or modify our configuration settings within your project!

.. list-table:: Presets for Various Executors in MIAAIM
   :widths: 25 25 25 25
   :header-rows: 1

   * - Flag
     - Excecution System / Workfload Manager
     - Memory
     - CPUs
   * - LSFsmall
     - LSF
     -
     -
   * - LSFmedium
     - LSF
     -
     -
   * - LSFbig
     - LSF
     -
     -
   * - LSFbig_multi
     - LSF
     -
     -
