import numpy as np
import argparse
import imutils
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help ="Path to the Image")
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original",image)


rotated = imutils.rotate(image,45,center=(50,40),scale=2.0)
cv2.imshow("rotated", rotated)
cv2.waitKey(0)
