##################################################
# Author: Dipam Patel
# Project: OpenCV - Operating on Image
# GitHub: ter.ps/dipam2
##################################################

# Importing Packages
import cv2
import numpy as np

# Reading Image
image = cv2.imread('pens.jpg')

# Fetching Color Value of a Random Pixel
pixel = image[100, 100]
print(pixel)

# Changing Color of a Random Pixel
image[200, 250] = [255, 255, 255]
pixel = image[200, 250]
print(pixel)

# Region of Image
roi = image[300:600, 500:800]
# print(roi)

# Changing the Region of Image
image[300:500, 500:700] = [255, 255, 255]
image[0:150, 0:250] = [255, 0, 0]

# Copy a Random Section of the Image
copy_section = image[50:350, 150:400]
image[500:800, 100:350] = copy_section

# # Displaying Image
cv2.imshow('Operated Image', image)

# # Saving Image
cv2.imwrite('Operated Image.jpg', image)

cv2.waitKey(0)
cv2.destroyAllWindows
