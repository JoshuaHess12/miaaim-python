.. _install to install:

Installation
============

MIAAIM is implemented in nextflow, which requires `Java 8 or later
<http://www.oracle.com/technetwork/java/javase/downloads/index.html>`_.
To install MIAAIM on your machine, follow the steps below for your operating system:


Linux / OS X
^^^^^^^^^^^^
1. `Install Docker <https://docs.docker.com/get-docker/>`_
and ensure that it is available to your system using the command :code:`docker images`

2. `Install Nextflow <https://www.nextflow.io>`_
using :code:`curl -s https://get.nextflow.io | bash`

3. You can check that Nextflow is installed by calling it in the context of the
directory that you installed it in with :code:`./nextflow run`.

4. (Recommended) If you want to be able to call Nextflow
directly from the command line without entering the path to it,
enter the follwing command::

   chmod +x nextflow    # be able to call nextflow

Windows
^^^^^^^
To run Nextflow in Windows, you will need to
`install WSL <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`_
prior to installing Nextflow. To do this, follow these steps:

1. Open Windows Powershell as administrator

2. Download WSL by typing
:code:`dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart`

3. Enable virtual machine by typing
:code:`dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart`

4. `Download <https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi>`_
the latest Linux kernel update package

5. Set WSL2 as your default kernel by typing :code:`wsl --set-default-version 2`

6. Install linux distribution -- we have tested MIAAIM successfully using
`Ubuntu 20.04 LTS <https://www.microsoft.com/store/apps/9n6svws3rx71>`_

7. Open your Ubuntu installation
(you will be asked to set up your installation by providing a user name and password)

8. Within the Ubuntu shell enter the following commands to install necessary
components for Nextflow and pulling the MIAAIM repository from GitHub::

   sudo apt update                           # upgrade packages
   sudo apt install openjdk-14-jre-headless  # install latest version of Java
   curl -s https://get.nextflow.io | bash    # install latest version of Nextflow
   chmod +x nextflow                         # be able to call nextflow
   sudo apt-get -y install git               # install git so you can clone MIAAIM from GitHub
   sudo apt-get install -y libarchive-tools  # install bsdtar command for unzipping prototype image

9. Now `install Docker <https://docs.docker.com/get-docker/>`_
for windows and allow it to connect with your WSL2 (see
`here <https://docs.docker.com/docker-for-windows/wsl/>`_ for details)

You should now be able to run nextflow and MIAAIM within your installed WSL as you
would with a Linux system (above) starting at step 3!

.. tip::
   You can transfer data to and from your WSL by using the :code:`/mnt` folder.
   For example, once inside your WSL, the following command will transfer the
   :code:`data-example` folder from the D drive on your windows machine to your home folder
   within the WSL::

      cp -r /mnt/d/data-example ~/           # copy data to WSL from D drive

Installing MIAAIM in Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you are interested in installing MIAAIM to use with Python, please navigate
to the :ref:`Python <Python to Python>` documentation.
