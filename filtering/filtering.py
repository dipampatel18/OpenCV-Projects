##################################################
# Author: Dipam Patel
# Project: OpenCV - Operating on Image
# GitHub: ter.ps/dipam2
##################################################

# Importing Packages
import cv2
import numpy as np

# Streaming Video from WebCam
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # HSV - Hue Saturation Value
    lower_red = np.array([150, 150,50])
    upper_red = np.array([180, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    # Displaying Live
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xff
    if k == 27:
        break


# Saving Image
# cv2.imwrite('Frame.jpg', frame)
# cv2.imwrite('Mask.jpg', mask)
# cv2.imwrite('Res.jpg', res)

cv2.destroyAllWindows()
cap.release()
