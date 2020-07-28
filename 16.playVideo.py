# importing libraries 
import cv2 
import numpy as np 

# Create a VideoCapture object and read from input file 
cap = cv2.VideoCapture('VideoSample.mp4') 

# Check if camera opened successfully 
if (cap.isOpened()== False): 
	print("Error opening video file") 

#Video Resolution
width = cap.get(3)
height = cap.get(4)
fps = cap.get(5)

print('Height: {}, Width: {}, fps: {}'.format(height,width,fps))

# Read until video is completed 
while(cap.isOpened()):
	# Capture frame-by-frame 
	ret, frame = cap.read() 

	#Get Height, Width and layers Information
	# height,width,layers =  frame.shape
	# print("Height: {}, Width: {}, Layers: {}".format(height,width,layers))

	if ret == True:
		#Resize Video Resolution to 540x960
		new_h=540
		new_w=960
		resize = cv2.resize(frame, (new_w, new_h))

		# Display the resulting resized frame 
		cv2.imshow('Frame', resize) 

		# Press Q on keyboard to exit 
		if cv2.waitKey(25) & 0xFF == ord('q'): 
			break

	# Break the loop 
	else: 
		break

# When everything done, release 
# the video capture object 
cap.release() 

# Closes all the frames 
cv2.destroyAllWindows() 
