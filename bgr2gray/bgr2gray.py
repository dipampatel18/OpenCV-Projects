##################################################
# Author: Dipam Patel
# Project: OpenCV - RGB to Gray
# GitHub: ter.ps/dipam2
##################################################

# Importing Packages
# import numpy as np
import cv2
# import matplotlib.pyplot as plt

# Reading Image
image = cv2.imread('pens.jpg')

## Method-1 ##
# Directly reading image in grayscale format
# gray_image = cv2.imread('pens.jpg', cv2.IMREAD_GRAYSCALE)

## Method-2 ##
# Converting color image to gray
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Showing Image
cv2.imshow('Gray Image', gray_image)

# Saving Image
cv2.imwrite('Gray Image.jpg', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
