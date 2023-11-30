from ultralytics import YOLO
import cv2

import numpy as np
detector = YOLO('best.pt')
cap = cv2.VideoCapture(0)
while cv2.waitKey(1) != 27:
    _, frame = cap.read()
    classes = detector(frame, verbose=False)[0]
    for obj in classes.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = obj
        x1, y1, x2, y2 = list(map(int, [x1, y1, x2, y2]))
        if score > 0.5:
            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
    cv2.imshow("frame", frame)

cv2.destroyAllWindows()