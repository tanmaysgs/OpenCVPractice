#A bilateral filter is used for smoothening images and reducing noise, 
# while preserving edges.

import cv2 

# Read the image. 
img = cv2.imread('./inputImages/taj.jpg') 

# Apply bilateral filter with d = 15, 
# sigmaColor = sigmaSpace = 75. 
bilateral = cv2.bilateralFilter(img, 15, 75, 75) 

# Save the output. 
#cv2.imwrite('taj_bilateral.jpg', bilateral) 
cv2.imshow('Original', img) 
cv2.imshow('Bilaterally filtered', bilateral) 

# De-allocate any associated memory usage 
if cv2.waitKey(0) & 0xff == 27: 
	cv2.destroyAllWindows() 
