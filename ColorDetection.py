import cv2
import numpy as np

def empty(v):
    return v

img = cv2.imread("Mario.jpg")
img = cv2.resize(img, (0, 0), fx=0.15, fy=0.15)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("img", img)
cv2.imshow("hsv", hsv)

#控制視窗
cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar", 640, 320)
cv2.createTrackbar("Hue min", "TrackBar", 0, 179, empty) # 0~179 default 0
cv2.createTrackbar("Hue max", "TrackBar", 255, 255, empty) # 0~255 default 255
cv2.createTrackbar("Sat min", "TrackBar", 0, 179, empty) # 0~179 default 0
cv2.createTrackbar("Sat max", "TrackBar", 255, 255, empty) # 0~255 default 255
cv2.createTrackbar("Val min", "TrackBar", 0, 179, empty) # 0~179 default 0
cv2.createTrackbar("Val max", "TrackBar", 255, 255, empty) # 0~255 default 255

while True:
    if ord("q") == cv2.waitKey(1):
        break

    Hue_min = cv2.getTrackbarPos("Hue min", "TrackBar")
    Hue_max = cv2.getTrackbarPos("Hue max", "TrackBar")
    Sat_min = cv2.getTrackbarPos("Sat min", "TrackBar")
    Sat_max = cv2.getTrackbarPos("Sat max", "TrackBar")
    Val_min = cv2.getTrackbarPos("Val min", "TrackBar")
    Val_max = cv2.getTrackbarPos("Val max", "TrackBar")

    print(Hue_min, Hue_max, Sat_min, Sat_max, Val_min, Val_max)

    lower = np.array([Hue_min, Sat_min, Val_min])
    upper = np.array([Hue_max, Sat_max, Val_max])
    #過濾顏色
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("mask", mask)
    cv2.imshow("img", result)

cv2.destroyAllWindows()