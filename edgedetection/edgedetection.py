##################################################
# Author: Dipam Patel
# Project: OpenCV - Operating on Image
# GitHub: ter.ps/dipam2
##################################################

# Importing Packages
import cv2
import numpy as numpy

# Streaming Video from WebCam
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    edges = cv2.Canny(frame, 100, 200)

    # Displaying Live
    cv2.imshow('Original', frame)
    cv2.imshow('Laplacian', laplacian)
    cv2.imshow('SobelX', sobelx)
    cv2.imshow('SobelY', sobely)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Saving Image
# cv2.imwrite('Original.jpg', frame)
# cv2.imwrite('Laplacian.jpg', laplacian)
# cv2.imwrite('Sobelx.jpg', sobelx)
# cv2.imwrite('Sobely.jpg', sobely)

cv2.destroyAllWindows()
cap.release()
