import cv2
import glob
import os
import numpy as np

# Get images
imgs = glob.glob('*.jpg')
print(f"Found {len(imgs)} images.")

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