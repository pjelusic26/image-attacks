import cv2
import glob
import os
import numpy as np
from pathlib import Path

# Source Directory
src_folder = 'TestSet/'
# Source Path
src_pth = Path(src_folder).resolve()


### SCALING ###
### SCALING ###
### SCALING ###
### SCALING ###

imgs = src_pth.glob('*.jpg')

# Wanted value of scaled image (in pixels)
width = 256
# Calculating the ratio of scaled and original image
width_str = str(width/512)
print(f"Resizing to {width} pixels, which is {width_str} of original.")

dst_folder = Path(src_folder+'/scaling/').resolve()
# Creating folder for scaled images
Path(dst_folder).mkdir(exist_ok=True)

# Iterate through scaling and saving
for img in imgs:
    # Naming image
    img_name = f"{str(dst_folder)}/scaling-{width_str}-{str(img.name)}"
    # Loads image as such including alpha channel
    pic = cv2.imread(str(img), cv2.IMREAD_UNCHANGED)
    # Defines height
    height = int(width * pic.shape[0] / pic.shape[1])
    # Scaling
    pic = cv2.resize(pic, (width, height))
    # Saving image
    cv2.imwrite(img_name, pic)

print("Done with scaling!")


### ROTATION ###
### ROTATION ###
### ROTATION ###
### ROTATION ###

imgs = src_pth.glob('*.jpg')

# Wanted value of rotation angle (in degrees)
angle = 45
print(f"Rotation by {angle} degrees.")

dst_folder = Path(src_folder+'/rotation/').resolve()
# Creating folder for rotated images
Path(dst_folder).mkdir(exist_ok=True)

# Iterate through rotation and saving
for img in imgs:
    # Naming image
    img_name = f"{str(dst_folder)}/rotation-{angle}-{str(img.name)}"
    # Loads image as such including alpha channel
    pic = cv2.imread(str(img), cv2.IMREAD_UNCHANGED)
    rows, cols = pic.shape[:2]
    # Defines center if image and angle of rotation
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    # Defines result image
    res = cv2.warpAffine(pic, M, (cols, rows))
    # Saving image
    cv2.imwrite(img_name, res)

print("Done with rotation!")


### AFFINE TRANSFORMATION ###
### AFFINE TRANSFORMATION ###
### AFFINE TRANSFORMATION ###
### AFFINE TRANSFORMATION ###

imgs = src_pth.glob('*.jpg')

# Defining points in original image
point_1_a = [50, 50]
point_1_b = [200, 50]
point_1_c = [50, 200]
# Defining points in transformed image
point_2_a = [10, 100]
point_2_b = [200, 50]
point_2_c = [100, 250]
print(
    f"Transforming from {point_1_a}, {point_1_b}, {point_1_c} to {point_2_a}, {point_2_b}, {point_2_c}.")

dst_folder = Path(src_folder+'/affine/').resolve()
# Creating folder for affine transformed images
Path(dst_folder).mkdir(exist_ok=True)

# Iterate through affine transform and saving
for img in imgs:
    # Naming image
    img_name = f"{str(dst_folder)}/affine-{str(img.name)}"
    # Loads image as such including alpha channel
    pic = cv2.imread(str(img), cv2.IMREAD_UNCHANGED)
    rows, cols, ch = pic.shape
    # Compiling original points into single array
    pts1 = np.float32([point_1_a, point_1_b, point_1_c])
    # Compiling transformed points into single array
    pts2 = np.float32([point_2_a, point_2_b, point_2_c])
    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(pic, M, (cols, rows))
    # Saving image
    cv2.imwrite(img_name, dst)

print("Done with affine transformation!")


### 2D CONVOLUTION ###
### 2D CONVOLUTION ###
### 2D CONVOLUTION ###
### 2D CONVOLUTION ###

imgs = src_pth.glob('*.jpg')

# Horizontal deviation (intensity)
kernel_x = 5
# Vertical deviation (intensity)
kernel_y = 5
kernel_x_str = str(kernel_x)
kernel_y_str = str(kernel_y)
kernel_multiplication = kernel_x * kernel_y
print(f"Convolution by {kernel_x}, {kernel_y}.")

dst_folder = Path(src_folder+'/convolution/').resolve()
# Creating folder for 2d convoluted images
Path(dst_folder).mkdir(exist_ok=True)

# Iterate through convolution and saving
for img in imgs:
    # Naming image
    img_name = f"{str(dst_folder)}/convolution-{kernel_x}x{kernel_y}-{str(img.name)}"
    # Loads image as such including alpha channel
    pic = cv2.imread(str(img), cv2.IMREAD_UNCHANGED)
    kernel = np.ones((kernel_x, kernel_y), np.float32)/kernel_multiplication
    dst = cv2.filter2D(pic, -1, kernel)
    # Saving image
    cv2.imwrite(img_name, dst)

print("Done with 2D convolution!")


### GAUSSIAN BLUR ###
### GAUSSIAN BLUR ###
### GAUSSIAN BLUR ###
### GAUSSIAN BLUR ###

imgs = src_pth.glob('*.jpg')

# Horizontal deviation (blur intensity)
kernel_x = 5
# Vertical deviation (blur intensity)
kernel_y = 5
kernel_x_str = str(kernel_x)
kernel_y_str = str(kernel_y)
print(f"Blurring by {kernel_x}, {kernel_y}.")

dst_folder = Path(src_folder+'/gaussian_blur/').resolve()
# Creating folder for blurred images
Path(dst_folder).mkdir(exist_ok=True)

# Iterate through blurring and saving
for img in imgs:
    # Naming image
    img_name = f"{str(dst_folder)}/gaussian_blur-{kernel_x}x{kernel_y}-{str(img.name)}"
    # Loads image as such including alpha channel
    pic = cv2.imread(str(img), cv2.IMREAD_UNCHANGED)
    dst = cv2.GaussianBlur(pic, (kernel_x, kernel_y), cv2.BORDER_DEFAULT)
    # Saving image
    cv2.imwrite(img_name, dst)

print("Done with gaussian blur!")


### GAUSSIAN NOISE ###
### GAUSSIAN NOISE ###
### GAUSSIAN NOISE ###
### GAUSSIAN NOISE ###

imgs = src_pth.glob('*.jpg')

# Wanted value of rotation angle (in degrees)
noise_amount = 0.5
print(f"Adding {noise_amount} noise.")

dst_folder = Path(src_folder+'/gaussian_noise/').resolve()
# Creating folder for noisy images
Path(dst_folder).mkdir(exist_ok=True)

# Iterate through noise-adding and saving
for img in imgs:
    # Naming image
    img_name = f"{str(dst_folder)}/gaussian_noise-{noise_amount}-{str(img.name)}"
    pic = cv2.imread(str(img), cv2.IMREAD_UNCHANGED)
    # Generate Gaussian noise
    gauss = np.random.normal(0, noise_amount, pic.size)
    gauss = gauss.reshape(
        pic.shape[0], pic.shape[1], pic.shape[2]).astype('uint8')
    # Add the Gaussian noise to the image
    img_gauss = cv2.add(pic, gauss)
    # Display the image
    cv2.imwrite(img_name, img_gauss)

print("Done with gaussian noise!")
