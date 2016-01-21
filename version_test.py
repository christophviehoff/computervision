import cv2
print ("Opencv Version {}".format(cv2.__version__))


for param in dir(cv2):
    if "XI" in param:
        print (param)

# Initialize camera

cam = cv2.VideoCapture(cv2.CAP_XIAPI)


while True:
    # Get an image
    flag, im = cam.read()

    # Received image
    if flag:
        # Show the image
        cv2.imshow("XIMEA cam", im)
        if cv2.waitKey(1) == ord('q'):
            break

    else:
        break

# Destroy windows and end program
cam.release()
cv2.destroyAllWindows()