##################################################
# Author: Dipam Patel
# Project: OpenCV - Arithmetics on Image
# GitHub: ter.ps/dipam2
##################################################

# Importing Packages
import cv2
import numpy as np

# Reading Image
image1 = cv2.imread('pens.jpg')
image2 = cv2.imread('universe.jpg')
image3 = cv2.imread('logo.jpg')

# Adding Two Images
add1 = image1 + image2  # None of the images lose their opaqueness
add2 = cv2.add(image1, image2)   # Their pixel values of both the images are added. 255 is the maximum limit.

# Adding Two Images based on their Weights
weighted = cv2.addWeighted(image1, 0.6, image2, 0.4, 10)    # image 1 percentage, image 2 percentage, gamma value

rows, cols, chan = image3.shape
roi = image1[0:rows, 0:cols]    # Defining the ROI in image1 based on the shape of image3

img2gray = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY) # Gray version of the logo
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)    # Pixel value above 220 would be converted to 255, else 0. Then it is inverted

mask_inv = cv2.bitwise_not(mask)

image3_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
image3_fg = cv2.bitwise_and(image3, image3, mask=mask)
 
dst = cv2.add(image3_bg, image3_fg)
image1[0:rows, 0:cols] = dst

# Displaying Image
cv2.imshow('Added Images - Directly', add1)
cv2.imshow('Added Images - Pixelwise', add2)
cv2.imshow('Weighted', weighted)
cv2.imshow('Result', image1)
cv2.imshow('Mask Inverse', mask_inv)
cv2.imshow('Image3 Background', image3_bg)
cv2.imshow('Image3 Foreground', image3_fg)
cv2.imshow('Dst', dst)

# Saving Images
cv2.imwrite('Direct Addition.jpg', add1)
cv2.imwrite('Pixelwise Addition.jpg', add2)
cv2.imwrite('Result.jpg', image1)
cv2.imwrite('Mask Inverse.jpg', mask_inv)
cv2.imwrite('Image3 Background.jpg', image3_bg)
cv2.imwrite('Image3 Foreground.jpg', image3_fg)
cv2.imwrite('Dst.jpg', dst)
cv2.imwrite('Weighted.jpg', weighted)

cv2.waitKey(0)
cv2.destroyAllWindows