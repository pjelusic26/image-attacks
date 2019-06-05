import cv2
import glob
import os
import numpy as np
from pathlib import Path

# source directory
src_folder = 'TestSet/'
# Source Path
src_pth = Path(src_folder).resolve()
imgs = src_pth.glob('*.jpg')

### SCALING ###
### SCALING ###
### SCALING ###
### SCALING ###

# Wanted value of resized image in pixels
width = 256
# Calculating the ratio of resized and original image
width_str = str(width/512)
print(f"Resizing to {width} pixels, which is {width_str} of original.")

dst_folder = Path(src_folder+'/scaling/').resolve()
# Creating folder for scaled images
Path(dst_folder).mkdir(exist_ok=True)

# Iterate through resizing and saving
for img in imgs:
    img_name = f"{str(dst_folder)}/scaling-{width_str}-{str(img.name)}"
    print(img_name)
    # Loads image as such including alpha channel
    pic = cv2.imread(str(img), cv2.IMREAD_UNCHANGED)
    # Defines height to be same as width => works for square images only
    height = int(width * pic.shape[0] / pic.shape[1])
    # Resizing
    pic = cv2.resize(pic, (width, height))
    cv2.imwrite(img_name, pic)        # Saving and naming image

print("Done scaling!")


### ROTATION ###
### ROTATION ###
### ROTATION ###
### ROTATION ###

# Wanted value of rotation angle (in degrees)
angle = 45
angle_str = str(angle)
print(f"Rotating by {angle} degrees.")

# Creating folder for rotated images
rotation_folder = 'rotation'
if not os.path.exists(rotation_folder):
    os.makedirs(rotation_folder)

# Iterate through resizing and saving
for img in imgs:
    # Loads image as such including alpha channel
    pic = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    rows, cols = pic.shape[:2]
    # Defines center if image and angle of rotation
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    # Defines result image
    res = cv2.warpAffine(pic, M, (cols, rows))
    cv2.imwrite(rotation_folder + '/' + 'rotation' + '-' +
                angle_str + '-' + img, res)  # Saving and naming image

print("Done rotating!")


### AFFINE TRANSFORMATION ###
### AFFINE TRANSFORMATION ###
### AFFINE TRANSFORMATION ###
### AFFINE TRANSFORMATION ###

# Defining points
point_1_a = [50, 50]
# nn original
point_1_b = [200, 50]
# image
point_1_c = [50, 200]

# Defining points
point_2_a = [10, 100]
# on transformed
point_2_b = [200, 50]
# image
point_2_c = [100, 250]
print(
    f"Transforming from {point_1_a}, {point_1_b}, {point_1_c} to {point_2_a}, {point_2_b}, {point_2_c}.")

# Creating folder for transformed images
affine_folder = 'affine_transformation'
if not os.path.exists(affine_folder):
    os.makedirs(affine_folder)

# Iterate through resizing and saving
for img in imgs:
    # Loads image as such including alpha channel
    pic = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    rows, cols, ch = pic.shape
    # Compiling original points into single array
    pts1 = np.float32([point_1_a, point_1_b, point_1_c])
    # Compiling transformed points into single array
    pts2 = np.float32([point_2_a, point_2_b, point_2_c])
    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(pic, M, (cols, rows))
    cv2.imwrite(affine_folder + '/' + 'affine_transformation' +
                '-' + img, dst)         # Saving and naming image

print("Done with affine transformation!")


### 2D CONVOLUTION ###
### 2D CONVOLUTION ###
### 2D CONVOLUTION ###
### 2D CONVOLUTION ###

# Horizontal deviation (blur intensity)
kernel_x = 5
# Vertical deviation (blur intensity)
kernel_y = 5
kernel_x_str = str(kernel_x)
kernel_y_str = str(kernel_y)
kernel_multiplication = kernel_x * kernel_y
print(f"Convoluting by {kernel_x}, {kernel_y}.")

# Creating folder for blurred images
convolution_2d_folder = 'convolution_2d'
if not os.path.exists(convolution_2d_folder):
    os.makedirs(convolution_2d_folder)

# Iterate through resizing and saving
for img in imgs:
    # Loads image as such including alpha channel
    pic = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    kernel = np.ones((kernel_x, kernel_y), np.float32)/kernel_multiplication
    dst = cv2.filter2D(pic, -1, kernel)
    cv2.imwrite(convolution_2d_folder + '/' + 'convolution_2d' + '-' + kernel_x_str +
                'x' + kernel_y_str + '-' + img, dst)               # Saving and naming image

print("Done with 2D convolution!")


### GAUSSIAN BLUR ###
### GAUSSIAN BLUR ###
### GAUSSIAN BLUR ###
### GAUSSIAN BLUR ###

# Horizontal deviation (blur intensity)
kernel_x = 5
# Vertical deviation (blur intensity)
kernel_y = 5
kernel_x_str = str(kernel_x)
kernel_y_str = str(kernel_y)
print(f"Blurring by {kernel_x}, {kernel_y}.")

# Creating folder for blurred images
gaussian_folder = 'gaussian_blur'
if not os.path.exists(gaussian_folder):
    os.makedirs(gaussian_folder)

# Iterate through resizing and saving
for img in imgs:
    # Loads image as such including alpha channel
    pic = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    dst = cv2.GaussianBlur(pic, (kernel_x, kernel_y), cv2.BORDER_DEFAULT)
    cv2.imwrite(gaussian_folder + '/' + 'gaussian_blur' + '-' + kernel_x_str +
                'x' + kernel_y_str + '-' + img, dst)               # Saving and naming image

print("Done with gaussian blur!")
