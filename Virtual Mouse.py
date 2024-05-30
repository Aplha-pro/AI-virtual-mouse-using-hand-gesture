import cv2
import numpy as np
import HandTrackingModule as htm
import time

cap = cv2.VideoCapture(0)  # 0 means our default camera
widthCam, heightCam = 640, 480

cap.set(3, widthCam)
cap.set(4, heightCam)

while True:
    success, img = cap.read()
    if success:
        cv2.imshow("Image", img)
        cv2.waitKey(1)
    else:
        break
