#!/usr/bin/env python3
import cv2
import numpy as np

class Window:
    def __init__(self, WIDTH=300, HEIGHT=150, WNAME="Track",pos=None):
        self.WNAME = WNAME
        HEIGHT = int(HEIGHT)
        WIDTH = int(WIDTH)
        self.frame = np.zeros((HEIGHT,WIDTH,3),np.uint8)
        cv2.namedWindow(WNAME)
        cv2.resizeWindow(WNAME, WIDTH, HEIGHT)
        if pos is not None:
            cv2.moveWindow(WNAME,pos[0],pos[1])
    def _nothing(self,x):
        return x
    def add_bar(self,name="",start=0,to=255):
        cv2.createTrackbar(name,self.WNAME,start,to,self._nothing)
    def __getitem__(self,name):
        return cv2.getTrackbarPos(name,self.WNAME)
    def show(self):
        cv2.imshow(self.WNAME,self.frame)
    def __setitem__(self,name,value):
        cv2.setTrackbarPos(name, self.WNAME, value)


wind = Window(500,500)
wind.add_bar("HL", 0, 180)
wind.add_bar("SL", 0, 255)
wind.add_bar("VL", 0, 255)

wind.add_bar("HH", 0, 180)
wind.add_bar("SH", 0, 255)
wind.add_bar("VH", 0, 255)

wind["HH"] = 180
wind["SH"] = 255
wind["VH"] = 255
img = cv2.imread("cub.jpg")
hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
while cv2.waitKey(1) != 27:
    frame = img.copy()
    lower_red = np.array([wind["HL"], wind["SL"], wind["VL"]])
    upper_red = np.array([wind["HH"], wind["SH"], wind["VH"]])
    mask = cv2.inRange(hsv_image, lower_red, upper_red)
    colored_area = cv2.bitwise_and(frame, frame, mask=mask)
    wind.frame = colored_area
    wind.show()
