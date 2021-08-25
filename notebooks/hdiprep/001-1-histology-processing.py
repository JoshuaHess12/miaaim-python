# testing modules for miaaim documentation

# -------------------Demonstrating HDIprep histology image processing-------------------
# import hdi utils module
import hdiutils.HDIimport.hdi_reader as hdi_reader
# import hdi_prep module
from miaaim.hdiprep.HDIprep import hdi_prep
# import external modules
import matplotlib.pyplot as plt
import os

import sys
sys.version

# set the path to the imaging data
path_to_im = "/Users/joshuahess/Desktop/prototype-001/input/fixed"
# set the path to the output directory
out_path = "/Users/joshuahess/Desktop/prototype-001/notebook-output"

# read data with HDIutils
fix_im = hdi_reader.HDIreader(
                    path_to_data=path_to_im,
                    path_to_markers=None,
                    flatten=False,
                    subsample=None,
                    mask=True,
                    save_mem=False
                    )
# create data set using HDIprep module
fix_dat = hdi_prep.IntraModalityDataset([fix_im])
# for plotting purposes, extract the key of the data set
key = list(fix_dat.set_dict.keys())[0]

# plot the histology image
plt.imshow(fix_dat.set_dict[key].hdi.data.image)
plt.savefig("/Users/joshuahess/Desktop/histology-prototype-001-1-raw.jpeg",bbox_inches='tight')
# plot the input manually drawn mask in ImageJ
plt.imshow(fix_dat.set_dict[key].hdi.data.mask.toarray(),cmap='gray')
plt.savefig("/Users/joshuahess/Desktop/histology-prototype-001-1-mask.jpeg",bbox_inches='tight')

# apply sequential processing steps
# remove salt and pepper noise
fix_dat.MedianFilter(filter_size=25,parallel=False)
# extract the procesed image to show
plt.imshow(fix_dat.set_dict[key].hdi.data.processed_image,cmap='gray')
plt.savefig("/Users/joshuahess/Desktop/histology-prototype-001-1-med1.jpeg",bbox_inches='tight')

# create mask with thresholding
fix_dat.Threshold(type='otsu')
# extract the procesed image to show
plt.imshow(fix_dat.set_dict[key].hdi.data.processed_image.toarray(),cmap='gray')
plt.savefig("/Users/joshuahess/Desktop/histology-prototype-001-1-thresh1.jpeg",bbox_inches='tight')

# morphological opening
fix_dat.Open(disk_size=20,parallel=False)
# extract the procesed image to show
plt.imshow(fix_dat.set_dict[key].hdi.data.processed_image.toarray(),cmap='gray')
plt.savefig("/Users/joshuahess/Desktop/histology-prototype-001-1-open1.jpeg",bbox_inches='tight')

# morphological closing
fix_dat.Close(disk_size=40,parallel=False)
# extract the procesed image to show
plt.imshow(fix_dat.set_dict[key].hdi.data.processed_image.toarray(),cmap='gray')
plt.savefig("/Users/joshuahess/Desktop/histology-prototype-001-1-close1.jpeg",bbox_inches='tight')

# morphological fill
fix_dat.Fill()
# extract the procesed image to show
plt.imshow(fix_dat.set_dict[key].hdi.data.processed_image.toarray(),cmap='gray')
plt.savefig("/Users/joshuahess/Desktop/histology-prototype-001-1-fill1.jpeg",bbox_inches='tight')

# morphological opening
fix_dat.Open(disk_size=15,parallel=False)
# extract the processed image to show
plt.imshow(fix_dat.set_dict[key].hdi.data.processed_image.toarray(),cmap='gray')
plt.savefig("/Users/joshuahess/Desktop/histology-prototype-001-1-open2.jpeg",bbox_inches='tight')

# apply the manual input mask (will act on the previous masks)
fix_dat.ApplyManualMask()
# extract the processed image to show
plt.imshow(fix_dat.set_dict[key].hdi.data.processed_image.toarray(),cmap='gray')
plt.savefig("/Users/joshuahess/Desktop/histology-prototype-001-1-manualmask.jpeg",bbox_inches='tight')

# extract bounding box in the image for constant padding
fix_dat.NonzeroBox()
# extract the processed image to show
plt.imshow(fix_dat.set_dict[key].hdi.data.processed_image.toarray(),cmap='gray')
plt.savefig("/Users/joshuahess/Desktop/histology-prototype-001-1-boxed.jpeg",bbox_inches='tight')

# apply the final mask after all operations
fix_dat.ApplyMask()
# extract the processed image to show
plt.imshow(fix_dat.set_dict[key].hdi.data.processed_image)
plt.savefig("/Users/joshuahess/Desktop/histology-prototype-001-1-final.jpeg",bbox_inches='tight')


# export the processed image to the nifti format for image registration
# here we pad the image for registration with the corresponding MSI
# compressed image.
fix_dat.ExportNifti1(
                    output_dir=out_path,
                    padding="(150,150)",
                    target_size=None
                    )

# load the exported image and view
exported = hdi_reader.HDIreader(
                    path_to_data=os.path.join(out_path,"fixed_processed.nii"),
                    path_to_markers=None,
                    flatten=False,
                    subsample=None,
                    mask=None,
                    save_mem=False
                    )
# plot the exported image
plt.imshow(exported.hdi.data.image)
plt.savefig("/Users/joshuahess/Desktop/histology-prototype-001-1-padded-final.jpeg",bbox_inches='tight')
