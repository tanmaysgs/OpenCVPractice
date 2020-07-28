# Edge Detection

import cv2 
import numpy as np 

FILE_NAME = './inputImages/dog.jpg'
try: 
	# Read image from disk. 
	img = cv2.imread(FILE_NAME) 

	# Canny edge detection. 
	edges = cv2.Canny(img, 100, 200) 

	# Write image back to disk. 
	cv2.imwrite('./outputImages/edgeDetection.jpg', edges) 

	cv2.imshow('Original Image', img)
	cv2.imshow('Contoured Image', edges)
  
	# De-allocate any associated memory usage   
	if cv2.waitKey(0) & 0xff == 27:  
	    cv2.destroyAllWindows()

except IOError: 
	print ('Error while reading files !!!') 
