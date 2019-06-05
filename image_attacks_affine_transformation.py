import cv2
import glob
import os
import numpy as np

# Get images
imgs = glob.glob('*.jpg')
print(f"Found {len(imgs)} images.")

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