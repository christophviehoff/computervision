import numpy as np
import argparse
import imutils
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help ="Path to the Image")
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original",image)


resized = imutils.resize(image,height= 100)
cv2.imshow("resized", resized)
cv2.waitKey(0)


flipped = imutils.flip(image,1)
cv2.imshow("flipped", flipped)
cv2.waitKey(0)
