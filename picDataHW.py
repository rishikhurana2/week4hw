import cv2
import numpy as np

fileLocation = "flag.svg.png"
file = "flag.svg.png"
img = cv2.imread(fileLocation)
Cimg = cv2.imread(file)
cv2.namedWindow("Original Image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("HSV Image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Threshold Image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Contour Image", cv2.WINDOW_AUTOSIZE)

cv2.imshow("Original Image", img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image", img_hsv)

THRESHOLD_MIN = np.array([0,200,0], np.uint8)
THRESHOLD_MAX = np.array([255,255,255], np.uint8)
frame_threshold = cv2.inRange(img_hsv, THRESHOLD_MIN, THRESHOLD_MAX)
frame_threshed = cv2.inRange(img_hsv, THRESHOLD_MIN, THRESHOLD_MAX) 
count = -1
image, contours, hierarchy = cv2.findContours(frame_threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(Cimg, contours, count, (255,255,255), 10)
cv2.imshow("Contour Image", Cimg)
cv2.imshow("Threshold Image", frame_threshold)
cv2.waitKey(0)
