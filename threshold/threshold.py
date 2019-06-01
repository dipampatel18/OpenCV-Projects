##################################################
# Author: Dipam Patel
# Project: OpenCV - Thresholding
# GitHub: ter.ps/dipam2
##################################################

# Importing Packages
import cv2
import numpy as np

# Reading Image
image = cv2.imread('book.jpg')

# Threshold 1
retval, threshold = cv2.threshold(image, 12, 255, cv2.THRESH_BINARY)

# Grayscale Conversion
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold 2
retval2, threshold2 = cv2.threshold(grayscale, 12, 255, cv2.THRESH_BINARY)

# Gaussian of Image
gaus = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

# OTSU
retval2, otsu = cv2.threshold(grayscale, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Displaying Image
cv2.imshow('Original', image)
cv2.imshow('Threshold 1', threshold)
cv2.imshow('Threshold 2', threshold2)
cv2.imshow('Gaussian', gaus)
cv2.imshow('OTSU', otsu)

# Saving Image
cv2.imwrite('Original.jpg', image)
cv2.imwrite('Threshold 1.jpg', threshold)
cv2.imwrite('Threshold 2.jpg', threshold2)
cv2.imwrite('Gaussian.jpg', gaus)
cv2.imwrite('OTSU.jpg', otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()