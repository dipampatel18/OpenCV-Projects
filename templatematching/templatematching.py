##################################################
# Author: Dipam Patel
# Project: OpenCV - RGB to Gray
# GitHub: ter.ps/dipam2
##################################################

# Importing Packages
import cv2
import numpy as np

# Reading Image
image_bg = cv2.imread('template.jpg')
template = cv2.imread('matching.jpg', 0)


image_gray = cv2.cvtColor(image_bg, cv2.COLOR_BGR2GRAY)
w, h = template.shape[::-1]

res = cv2.matchTemplate(image_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.90
loc = np.where(res >= threshold)

# Drawing Rectangle around the Matching Area
for pt in zip(*loc[::-1]):
    cv2.rectangle(image_bg, pt, (pt[0]+w, pt[1]+h), (0, 255, 0), 2)

# Displaying the Image
cv2.imshow('Detected', image_bg)

# Saving the Image
cv2.imwrite('Detected.jpg', image_bg)

cv2.waitKey(0)
cv2.destroyAllWindows()
