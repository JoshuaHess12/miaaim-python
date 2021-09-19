# testing modules for miaaim documentation

# -------------------Demonstrating HDIreg image registration-------------------
# import hdi utils module
import hdiutils.HDIimport.hdi_reader as hdi_reader
# import elastix and transformix modules
from miaaim.hdiprep.HDIprep import hdi_prep
from miaaim.hdireg.HDIreg import elastix
from miaaim.hdireg.HDIreg import transformix
# import external modules
import matplotlib.pyplot as plt
import os

import sys
sys.version

# set the path to the processed imaging data from hdiprep modules
path_to_fixed = r"D:\Josh_Hess\prototype-001\notebook-output\fixed_processed.nii"
path_to_moving = r"D:\Josh_Hess\prototype-001\notebook-output\moving_processed.nii"
# set the path to the output directory
out_dir = r"D:\Josh_Hess\prototype-001\notebook-output"

# read data with HDIutils
fix_im = hdi_reader.HDIreader(
                    path_to_data=path_to_fixed,
                    path_to_markers=None,
                    flatten=False,
                    subsample=None,
                    mask=False,
                    save_mem=False
                    )
# create data set using HDIprep module
fix_dat = hdi_prep.IntraModalityDataset([fix_im])
# for plotting purposes, extract the key of the data set
fix_key = list(fix_dat.set_dict.keys())[0]

# read data with HDIutils
mov_im = hdi_reader.HDIreader(
                    path_to_data=path_to_moving,
                    path_to_markers=None,
                    flatten=False,
                    subsample=None,
                    mask=False,
                    save_mem=False
                    )
# create data set using HDIprep module
mov_dat = hdi_prep.IntraModalityDataset([mov_im])
# for plotting purposes, extract the key of the data set
mov_key = list(mov_dat.set_dict.keys())[0]

# plot the histology image
plt.imshow(fix_dat.set_dict[fix_key].hdi.data.image)
# plot the moving steady state UMAP compressed image (note that we are only showing
# the first three channels in RGB space)
plt.imshow(mov_dat.set_dict[mov_key].hdi.data.image[:,:,:3])

# set path to affine registration parameters
affine_pars = r"D:\Josh_Hess\prototype-001\input\affine_short.txt"
# set path to affine registration parameters
nonlinear_pars = r"D:\Josh_Hess\prototype-001\input\nonlinear_short.txt"
# concatenate the two parameter files to a list
p = [affine_pars, nonlinear_pars]

# run the registration
elastix.Elastix(path_to_fixed,
                path_to_moving,
                out_dir,
                p,
                fp=None,
                mp=None,
                fMask=None
                )

# set path to output image
result_path = r"D:\Josh_Hess\prototype-001\notebook-output\elastix-fiji-stack.tif"
# read the output image stack for registration results
result = hdi_reader.HDIreader(
                    path_to_data=result_path,
                    path_to_markers=None,
                    flatten=False,
                    subsample=None,
                    mask=False,
                    save_mem=False
                    )
# create data set using HDIprep module
result_dat = hdi_prep.IntraModalityDataset([result])
# for plotting purposes, extract the key of the data set
result_key = list(result_dat.set_dict.keys())[0]

# plot the histology image
plt.imshow(result_dat.set_dict[result_key].hdi.data.image)

# set path to moving image
in_im = r"D:\Josh_Hess\prototype-001\input\moving"
# set path to output transform parameter files
tps = [r"D:\Josh_Hess\prototype-001\notebook-output\TransformParameters.0.txt",
        r"D:\Josh_Hess\prototype-001\notebook-output\TransformParameters.1.txt"]
# set target size and padding (see notebook 001 for details)
target_size = (2472,1572)
pad = (20,20)

# transform the set of MSI data
transformix.Transformix(in_im,
                        out_dir,
                        tps,
                        target_size,
                        pad,
                        trim = None,
                        crops = None,
                        out_ext = ".nii"
                        )










#
