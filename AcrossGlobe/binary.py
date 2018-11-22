import cv2
import numpy as np

image = cv2.imread('test.jpg',0)
#mser = cv2.MSER_create()

#img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
vis=image.copy()
kernel = np.ones((2,2),np.uint8)
median = cv2.medianBlur(image,3)

retval, threshold = cv2.threshold(median, 110, 255, cv2.THRESH_BINARY)
erosion = cv2.erode(threshold,kernel,iterations = 1)
#dilation = cv2.dilate(threshold,kernel,iterations = 1)
#median = cv2.medianBlur(threshol,5)
#regions = mser.detectRegions(threshold)
#hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions[0]]
#cv2.polylines(vis, hulls, 1, (0,255,0)) 

cv2.imshow('original',image)
#cv2.imshow('final',vis)
cv2.imshow('Median',median)
#cv2.imshow('threshold',threshold)
cv2.waitKey(0)
