# Read Libraries
import numpy as np
import cv2

# Reading Image
img = cv2.imread('../inputImages/dog.jpg', 0)

# will show the image in a window 
cv2.imshow('image', img) 
k = cv2.waitKey(0) & 0xFF
  
# wait for ESC key to exit 
if k == 27:  
    cv2.destroyAllWindows() 
      
# wait for 's' key to save and exit 
elif k == ord('s'):  
    cv2.imwrite('./outputImages/messigray.png',img) 
    cv2.destroyAllWindows()