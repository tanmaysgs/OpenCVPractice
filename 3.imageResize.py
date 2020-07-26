#https://www.geeksforgeeks.org/image-resizing-using-opencv-python

#Image Resizing
import cv2 
import numpy as np 
import matplotlib.pyplot as plt  
# % matplotlib qt 
# This is a magic command to display in an external window 
  
image = cv2.imread("./inputImages/ghost.jpg", 1) 
imageShape = image.shape
# Loading the image 
  
half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1) 
bigger = cv2.resize(image, (1050, 1610)) 
  
stretch_near = cv2.resize(image, (780, 540),  
               interpolation = cv2.INTER_NEAREST) 
  
  
# Titles =["Original", "Half", "Bigger", "Interpolation Nearest"] 
# images =[image, half, bigger, stretch_near] 

print("Original Image Shape: ",imageShape)

#Display Images
cv2.imshow('Original Image', image)
cv2.imshow('Half Image', half)
cv2.imshow('Bigger Image', bigger)
cv2.imshow('Interpolation Image', stretch_near)
  
# De-allocate any associated memory usage   
if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()