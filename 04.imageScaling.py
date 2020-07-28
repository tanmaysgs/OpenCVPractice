# Image Scaling
import cv2 
import numpy as np 

FILE_NAME = './inputImages/dog.jpg'
try: 
	# Read image from disk. 
	img = cv2.imread(FILE_NAME) 

	# Get number of pixel horizontally and vertically. 
	(height, width) = img.shape[:2] 

	# Specify the size of image along with interploation methods. 
	# cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_CUBIC 
	# is used for zooming. 
	res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC) 

	# Write image back to disk. 
	cv2.imwrite('./outputImages/rescaled.jpg', res) 

	cv2.imshow('Original Image', img)
	cv2.imshow('Rescaled Image', res)
  
	# De-allocate any associated memory usage   
	if cv2.waitKey(0) & 0xff == 27:  
	    cv2.destroyAllWindows()
except IOError: 
	print ('Error while reading files !!!') 
