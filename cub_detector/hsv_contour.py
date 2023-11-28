import cv2
import numpy as np


def get_bbox(mask):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with the maximum area
    largest_contour = max(contours, key=cv2.contourArea)

    # Get the bounding box coordinates of the largest contour
    x, y, w, h = cv2.boundingRect(largest_contour)

    # Draw the bounding box on the original image
    return x, y, w, h


image = cv2.imread("cub.jpg") # read the image
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # convert image from BGR to HSV

lower1 = np.array([0, 100, 20])
upper1 = np.array([10, 255, 255])

lower2 = np.array([160,100,20])
upper2 = np.array([179,255,255])

lower_mask = cv2.inRange(hsv, lower1, upper1) # apply range1

upper_mask = cv2.inRange(hsv, lower2, upper2) # apply range2

full_mask = cv2.bitwise_or(lower_mask, upper_mask) #bitwise_or to both masks

eroded_mask = cv2.erode(full_mask, None, iterations=4)
x,y,w,h = get_bbox(eroded_mask)
cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)
cv2.imshow('image', image)
# cv2.imshow('extracted', full_mask)
cv2.waitKey(0)