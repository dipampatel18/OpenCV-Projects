##################################################
# Author: Dipam Patel
# Project: OpenCV - Drawing on Image
# GitHub: ter.ps/dipam2
##################################################

# Importing Packages
import cv2
import numpy as np

# Reading Image
image = cv2.imread('pens.jpg', cv2.IMREAD_COLOR)

# Drawing a Line
cv2.line(image, (400,800), (800, 500), (255, 0, 0), 5)  # start, end, color, thickness

# Drawing a Rectangle
cv2.rectangle(image, (10, 20), (200, 300), (0, 255, 0), 10) # top left corner, bottom right corner, color, thickness / fill color

# Drawing a Circle
cv2.circle(image, (500, 500), 80, (0, 0, 255), -1 ) # center, radius, color, thickness / fill color

# Drawing a Polygon
points = np.array([[50, 500],[300, 400],[350, 500]], np.int32)  # x,y points, data type
cv2.polylines(image, [points], True, (0, 255, 255), 5)  # True / False to close the polygon, color, thickness

# Displaying Text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'OpenCV Text', (300, 100), font, 2, (255, 255, 255), 5, cv2.LINE_AA)

# Showing Image
cv2.imshow('New Image', image)

# Saving Image
cv2.imwrite('New Image.jpg', image)

cv2.waitKey(0)
cv2.destroyAllWindows