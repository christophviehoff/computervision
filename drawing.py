import numpy as np
import cv2


canvas = np.zeros((300,300,3),dtype="uint8")
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

green = (0,255,0)

cv2.line(canvas, (0,0),(300,300),green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)



red = (0,0,255) #bgr

cv2.line(canvas, (300,0),(0,300),red,3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255,0,0)

cv2.rectangle(canvas, (10,10),(60,60),blue,-1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# circle example
canvas = np.zeros((300,300,3),dtype="uint8")
(centerX, centerY) = (int(canvas.shape[1] / 2),int( canvas.shape[0] / 2))
white =(255,255,255)


#print ((centerX,centerY))  requiered interegr as input

for r in range(0,175,25):
	cv2.circle(canvas, (centerX,centerY), r, white)
	
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#abstract

for i in range(0,25):
	radius = np.random.randint(5, high=200)
	color = np.random.randint(0,high=256,size =(3,)).tolist()
	
	pt = np.random.randint(0,high=300,size=(2,))
	
	cv2.circle(canvas, tuple(pt), radius, color, -1)


cv2.imshow("Canvas", canvas)
cv2.waitKey(0)	
	
	
	
	

