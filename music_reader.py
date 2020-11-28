import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from skimage.color import rgb2gray
from misc_fns import *

sheet = plt.imread('overworld_2staff.png')
#sheet = plt.imread('overworld.png')

#Convert image to binary
bin_sheet = rgba2rgb(sheet)
bin_sheet = rgb2gray(bin_sheet)
print(bin_sheet.shape)
print(bin_sheet.shape[1])
bin_sheet = gray2binary(bin_sheet)

#Staff finder
staff = erode(bin_sheet,1,30)
staff = dilation(staff,1,30)

#Difference between staff and orignal binary
diff = np.subtract(bin_sheet,staff)
print(diff)

#Display image
f, axarr = plt.subplots(2,2)
axarr[0,0].set_title("Original")
axarr[0,0].imshow(sheet)
axarr[0,1].set_title("Erosion then dilation")
axarr[0,1].imshow(staff, cmap=plt.cm.gray)
axarr[1,0].set_title("Diff")
axarr[1,0].imshow(diff, cmap=plt.cm.gray)
axarr[1,1].set_title("Binary")
axarr[1,1].imshow(bin_sheet, cmap=plt.cm.gray)

plt.show()