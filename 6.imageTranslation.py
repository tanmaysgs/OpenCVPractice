#Translating an image, shifting an image
import cv2 
import numpy as np 

FILE_NAME = './inputImages/dog.jpg'

# Create translation matrix. 
# If the shift is (x, y) then matrix would be 
# M = [1 0 x] 
#	 [0 1 y] 
# Let's shift by (100, 50). 
M = np.float32([[1, 0, 100], [0, 1, 50]]) 

try: 

	# Read image from disk. 
	img = cv2.imread(FILE_NAME) 
	(rows, cols) = img.shape[:2] 

	# warpAffine does appropriate shifting given the 
	# translation matrix. 
	res = cv2.warpAffine(img, M, (cols, rows)) 

	# Write image back to disk. 
	cv2.imwrite('./outputImages/translated.jpg', res) 

	cv2.imshow('Original Image', img)
	cv2.imshow('Shifted Image', res)
  
	# De-allocate any associated memory usage   
	if cv2.waitKey(0) & 0xff == 27:  
	    cv2.destroyAllWindows()

except IOError: 
	print ('Error while reading files !!!') 
