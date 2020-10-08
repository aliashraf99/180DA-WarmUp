import numpy as np
import cv2


#cap = cv2.VideoCapture(0)

#while(True):
    # Capture frame-by-frame
 #   ret, frame = cap.read()

    # Our operations on the frame come here
  #  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
   # ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    
    # Display the resulting frame
    #cv2.imshow('frame',thresh)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
     #   break

# When everything done, release the capture
#cap.release()
#cv2.destroyAllWindows()

#code adapted from OpenCV tutorial website
cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_red = np.array([0,70,50])
    upper_red = np.array([10,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)


    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()