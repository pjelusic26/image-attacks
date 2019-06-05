import cv2
import glob
import os
import numpy as np

# Get images
imgs = glob.glob('*.jpg')
print(f"Found {len(imgs)} images.")

### 2D CONVOLUTION ###
### 2D CONVOLUTION ###
### 2D CONVOLUTION ###
### 2D CONVOLUTION ###

kernel_x = 5                                                                            # Horizontal deviation (blur intensity)
kernel_y = 5                                                                            # Vertical deviation (blur intensity)
kernel_x_str = str(kernel_x)
kernel_y_str = str(kernel_y)
kernel_multiplication = kernel_x * kernel_y
print(f"Convoluting by {kernel_x}, {kernel_y}.")

convolution_2d_folder = 'convolution_2d'                                                # Creating folder for blurred images
if not os.path.exists(convolution_2d_folder):
    os.makedirs(convolution_2d_folder)

# Iterate through resizing and saving
for img in imgs:
    pic = cv2.imread(img, cv2.IMREAD_UNCHANGED)                                         # Loads image as such including alpha channel
    kernel = np.ones((kernel_x, kernel_y),np.float32)/kernel_multiplication
    dst = cv2.filter2D(pic,-1,kernel)
    cv2.imwrite(convolution_2d_folder + '/' + 'convolution_2d' + '-' + kernel_x_str + 'x' + kernel_y_str + '-' + img, dst)               # Saving and naming image

print("Done with 2D convolution!")