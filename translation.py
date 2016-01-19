import numpy as np
import argparse
import imutils
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help ="Path to the Image")
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original",image)

#translation    1,0,tx   0,1,ty   
M= np.float32([[1,0,25],[0,1,50]])

shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))

cv2.imshow("shifted Down and Right", shifted)
cv2.waitKey(0)

shifted = imutils.translate(image,0,100)
cv2.imshow("shifted down", shifted)
cv2.waitKey(0)


