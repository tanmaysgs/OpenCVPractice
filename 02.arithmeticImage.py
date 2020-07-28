# Add and Subtract two images

# Python programe to illustrate  
# arithmetic operation of 
# addition of two images 
    
# organizing imports  
import cv2  
import numpy as np  
    
# path to input images are specified and   
# images are loaded with imread command  
image1 = cv2.imread('./inputImages/image1.jpg')  
image2 = cv2.imread('./inputImages/image2.jpg') 
  
# Adding images without any weights
# addedImage= cv2.add(image1,image2)

# cv2.addWeighted is applied over the  image inputs with applied parameters 
weightedSum = cv2.addWeighted(image1, 0.6, image2, 0.3, 0) 
  
# the window showing output image 
# with the weighted sum  
cv2.imshow("First Image", image1)
cv2.imshow("Second Image", image2)
# cv2.imshow('Added Image', addedImage) 
cv2.imshow('Weighted Image', weightedSum) 
  
# De-allocate any associated memory usage   
if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()