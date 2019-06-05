import cv2
import glob
import os
import numpy as np

# Get images
imgs = glob.glob('*.jpg')
print(f"Found {len(imgs)} images.")




### SCALING ###
### SCALING ###
### SCALING ###
### SCALING ###

width = 256                                                                         # Wanted value of resized image in pixels
width_str = str(width/512)                                                          # Calculating the ratio of resized and original image
print(f"Resizing to {width} pixels, which is {width_str} of original.")

folder = 'scaling'                                                                  # Creating folder for scaled images
if not os.path.exists(folder):
    os.makedirs(folder)

# Iterate through resizing and saving
for img in imgs:
    pic = cv2.imread(img, cv2.IMREAD_UNCHANGED)                                     # Loads image as such including alpha channel
    height = int(width * pic.shape[0] / pic.shape[1])                               # Defines height to be same as width => works for square images only
    pic = cv2.resize(pic, (width, height))                                          # Resizing
    cv2.imwrite(folder + '/' + 'scaling' + '-' + width_str + '-' + img, pic)        # Saving and naming image

print("Done scaling!") 




### ROTATION ###
### ROTATION ###
### ROTATION ###
### ROTATION ###

angle = 45                                                                              # Wanted value of rotation angle (in degrees)
angle_str = str(angle)
print(f"Rotating by {angle} degrees.")

rotation_folder = 'rotation'                                                            # Creating folder for rotated images
if not os.path.exists(rotation_folder):
    os.makedirs(rotation_folder)

# Iterate through resizing and saving
for img in imgs:
    pic = cv2.imread(img, cv2.IMREAD_UNCHANGED)                                         # Loads image as such including alpha channel
    rows, cols = pic.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)                         # Defines center if image and angle of rotation
    res = cv2.warpAffine(pic, M, (cols, rows))                                          # Defines result image
    cv2.imwrite(rotation_folder + '/' + 'rotation' + '-' + angle_str + '-' + img, res)  # Saving and naming image

print("Done rotating!")




### AFFINE TRANSFORMATION ###
### AFFINE TRANSFORMATION ###
### AFFINE TRANSFORMATION ###
### AFFINE TRANSFORMATION ###

point_1_a = [50,50]                                                                     # Defining points
point_1_b = [200,50]                                                                    # nn original
point_1_c = [50,200]                                                                    # image

point_2_a = [10,100]                                                                    # Defining points
point_2_b = [200,50]                                                                    # on transformed
point_2_c = [100,250]                                                                   # image
print(f"Transforming from {point_1_a}, {point_1_b}, {point_1_c} to {point_2_a}, {point_2_b}, {point_2_c}.")

affine_folder = 'affine_transformation'                                                 # Creating folder for transformed images
if not os.path.exists(affine_folder):
    os.makedirs(affine_folder)

# Iterate through resizing and saving
for img in imgs:
    pic = cv2.imread(img, cv2.IMREAD_UNCHANGED)                                         # Loads image as such including alpha channel
    rows, cols, ch = pic.shape
    pts1 = np.float32([point_1_a, point_1_b, point_1_c])                                # Compiling original points into single array
    pts2 = np.float32([point_2_a, point_2_b, point_2_c])                                # Compiling transformed points into single array
    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(pic, M, (cols,rows))
    cv2.imwrite(affine_folder + '/' + 'affine_transformation' + '-' + img, dst)         # Saving and naming image

print("Done with affine transformation!")




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