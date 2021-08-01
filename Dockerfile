FROM superelastix/elastix:5.0.1 AS elastix

COPY . /app/

RUN apt update && apt -y upgrade
RUN apt install python3.8 -y
RUN apt-get update && apt-get install -y python3-pip
RUN apt-get -y install git
RUN ln -sf /usr/bin/pip3 /usr/bin/pip
RUN ln -sf /usr/bin/python3.8 /usr/bin/python

RUN pip3 install install scikit-image numpy pandas pyimzml nibabel scipy h5py pathlib umap-learn uncertainties seaborn matplotlib scikit-learn PyYAML

RUN pip3 install "dask[complete]"

RUN pip3 install -e git+https://github.com/JoshuaHess12/hdi-utils.git@main#egg=hdi-utils
RUN pip3 install miaaim-python
