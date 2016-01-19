from __future__ import print_function
import argparse
import cv2


ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help ="Path to the Image")
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original",image)


(b, g, r) = image[0,0]

print ("Pixel at (0,0) - Red: {}, Green: {}, Blue {}".format(r,g,b))

image[0,0] = (0,0,255)
(b, g, r) = image[0,0]

print ("Pixel at (0,0) - Red: {}, Green: {}, Blue {}".format(r,g,b))


width=image.shape[1]
height=image.shape[0]

print ("width: {} pixels".format(image.shape[1]))
print ("height: {} pixels".format(image.shape[0]))

corner = image[0:height/2,0:width/2]

cv2.imshow("Corner",corner)
	
image[0:height/2,0:width/2]= (0,255,0)

cv2.imshow("Updated", image)
cv2.waitKey(0)
