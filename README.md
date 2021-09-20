# MIAAIM: multi-omics image alignment and analysis by information manifolds
MIAAIM is a software to align multiple-omics tissue imaging data. The worflow includes high-dimensional image compression, registration, and transforming images to align in the same spatial domain. MIAAIM was developed at the [Vaccine and Immunotherapy Center at MGH](http://advancingcures.org) in the labs of [Dr. Patrick Reeves](http://advancingcures.org/reeves-lab/) and [Dr. Ruxandra Sîrbulescu](http://advancingcures.org/sirbulescu-lab/).

For further documentation on the MIAAIM Python impementation, please visit [joshuahess12.github.io/miaaim-python](https://joshuahess12.github.io/miaaim-python/).

## Installation
You can install MIAAIM in Python using either the MIAAIM-Python Docker container, which would allow for complete workflow
reproducibility, or you can install the package into your environment with pip.

### Dependencies
MIAAIM utilizes the [Elastix](https://elastix.lumc.nl) library for image registration computations, which is written in the C++ language. For this reason, we recommend running your workflows with the MIAAIM Python package inside of a Docker container, which we have created to automatically include Elastix. You can still run MIAAIM, however, if you would rather stick with installing packages via pip, you will just need to install Elastix separately. These two options for installing MIAAIM are outlined below:

### Usage without Docker / Install with Pip:
If you are unable to use Docker on your machine, then you can still use MIAAIM:
1. [download](https://github.com/SuperElastix/elastix/releases/tag/5.0.1) the latest version of Elastix.
2. Make Elastix accessible to your `$PATH` environment (Ex. on a Mac, access your `.bash_profile` and add `export PATH=~/elastix-latest/bin:$PATH` and `export DYLD_LIBRARY_PATH=~/elastix-latest/lib:$DYLD_LIBRARY_PATH`)
3. Run the following command to install MIAAIM on your machine:
```bash
 pip install miaaim-python  # install miaaim
 ```

#### Reproducibility with Pip
If you are using pip to install MIAAIM, you can reconstruct your working environment easily with the commands:
1.
```bash
 pip freeze > requirements.txt  # create documentation of installed packages
 ```
This will create a text file that indicates the specific packages that you are using. You can then
install the specific packages that were exported into another environment with :
2.
```bash
pip install -r requirements.txt
```
We have included a `requirements.txt` file in this repository to use for our convenience.

### Docker
MIAAIM's Python implementation is containerized using Docker to enable a reproducible environment. Inside of this container,
the Python distribution of MIAAIM is already installed. It is therefore set up so that users can copy scripts and data into it in order to run analyses that they need.

To get started with MIAAIM using Docker:
1. [Install Docker](https://docs.docker.com/get-docker/).
2. Ensure that Docker is available to your system using the command `docker images`
3. Pull the miaaim-python docker container `docker pull joshuahess/miaaim-python:latest` where `latest` is the version number.

#### Using MIAAIM inside of Docker
If you are using MIAAIM with Docker, we recommend having a concrete file structure for data and code with relative paths so that your script doesn't rely on absolute file paths outside of the Docker container.

You can mount your custom scripts and data into the virtual environment as follows:
4. Mount your data and scripts into Docker from your local path (`src-path`)
```bash
docker run -it -v /path/to/data:/data joshuahess/miaaim-python:latest bash    # mount data in the "dest-path" folder
```
Here, we assumed that the folder `data` contains your new script and your input data that goes with it.
5. Run your script (named here `script.py`) from the data folder:
```bash
python ./data/scipt.py
```
Note here that any additional packages that you use to process your data that are not included in the docker image will not be found!
