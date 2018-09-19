# Python program for Detection of a 
# specific color(blue here) using OpenCV with Python
import cv2
import numpy as np

def getColorMap(name):

    frame = cv2.imread(name)
    # Converts images from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low = np.array([25, 15, 150])
    high = np.array([154, 137, 251])

    # Here we are defining range of bluecolor in HSV
    # This creates a mask of blue coloured
    # objects found in the frame.
    mask = cv2.inRange(frame, low, high)

    # The bitwise and of the frame and mask is done so
    # that only the blue coloured objects are highlighted
    # and stored in res
    #res = cv2.bitwise_and(frame, frame, mask=mask)

    #cv2.imshow('frame', frame)
    kernelOpen = np.ones((5, 5))
    kernelClose = np.ones((20, 20))

    maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelOpen)
    maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernelClose)

    frame_w = 300
    mask = cv2.resize(mask, (frame_w,frame_w))
    maskClose = cv2.resize(maskClose, (frame_w,frame_w))
    maskOpen = cv2.resize(maskOpen, (frame_w,frame_w))

    cv2.imshow(name + "Close", maskClose)
    cv2.imshow(name + "Mask", mask)
    cv2.imshow(name + "Open", maskOpen)

    # This displays the frame, mask
    # and res which we created in 3 separate windows.

getColorMap("trucks/truck1.jpg")
getColorMap("trucks/truck2.jpg")
getColorMap("trucks/truck3.jpg")
cv2.waitKey(0)