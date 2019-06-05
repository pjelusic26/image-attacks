import cv2
import glob
import os
import numpy as np

# Get images
imgs = glob.glob('*.jpg')
print(f"Found {len(imgs)} images.")

### GAUSSIAN BLUR ###
### GAUSSIAN BLUR ###
### GAUSSIAN BLUR ###
### GAUSSIAN BLUR ###

kernel_x = 5                                                                            # Horizontal deviation (blur intensity)
kernel_y = 5                                                                            # Vertical deviation (blur intensity)
kernel_x_str = str(kernel_x)
kernel_y_str = str(kernel_y)
print(f"Blurring by {kernel_x}, {kernel_y}.")

gaussian_folder = 'gaussian_blur'                                                       # Creating folder for blurred images
if not os.path.exists(gaussian_folder):
    os.makedirs(gaussian_folder)

# Iterate through resizing and saving
for img in imgs:
    pic = cv2.imread(img, cv2.IMREAD_UNCHANGED)                                         # Loads image as such including alpha channel
    dst = cv2.GaussianBlur(pic,(kernel_x, kernel_y),cv2.BORDER_DEFAULT)
    cv2.imwrite(gaussian_folder + '/' + 'gaussian_blur' + '-' + kernel_x_str + 'x' + kernel_y_str + '-' + img, dst)               # Saving and naming image

print("Done with gaussian blur!")