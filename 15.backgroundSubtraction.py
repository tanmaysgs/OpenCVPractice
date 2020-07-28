# Background Subtraction has several use cases in everyday life, 
# It is being used for object segmentation, security enhancement, 
# tracking, counting the number of visitors, number of vehicles in traffic etc. 
# It is able to learn and identify the foreground mask.

# The popular Background subtraction algorithms are:

# BackgroundSubtractorMOG : It is a gaussian mixture based background segmentation algorithm.
# BackgroundSubtractorMOG2: It uses the same concept but the major advantage that it provides is in terms of stablity even when there is change in luminosity and better identification capablity of shadows in the frames.
# Geometric multigrid: It makes uses of statiistical method and per pixel bayesin segmentation algorithm.

# Python code for Background subtraction using OpenCV 
import numpy as np 
import cv2 

cap = cv2.VideoCapture(0) 
fgbg = cv2.createBackgroundSubtractorMOG2() 

while(1): 
	ret, frame = cap.read() 

	fgmask = fgbg.apply(frame) 

	cv2.imshow('fgmask', fgmask) 
	cv2.imshow('frame',frame ) 

	
	k = cv2.waitKey(30) & 0xff
	if k == 27: 
		break
	

cap.release() 
cv2.destroyAllWindows() 
