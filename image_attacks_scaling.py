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