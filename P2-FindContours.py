import cv2 
import numpy as np 

# Let's load a simple image 
image = cv2.imread('./inputImages/stop.jpg')  

# Grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

# Find Canny edges 
edged = cv2.Canny(gray, 30, 200) 

cv2.imshow('Original',image)
cv2.imshow('Grayscale',gray)
cv2.imshow('Edged',edged)
# Finding Contours 
# Use a copy of the image e.g. edged.copy() 
# since findContours alters the image 
_,contours, hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

cv2.imshow('Canny Edges After Contouring', edged) 
# cv2.waitKey(0) 

print("Number of Contours found = " + str(len(contours))) 

# Draw all contours 
# -1 signifies drawing all contours 
cv2.drawContours(image, contours, -1, (0, 255, 0), 3) 

cv2.imshow('Contours', image) 

# Exiting the window if 'q' is pressed on the keyboard. 
if cv2.waitKey(0) & 0xFF == ord('q'): 
	cv2.destroyAllWindows() 