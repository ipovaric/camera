# https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/#

import cv2

vid = cv2.VideoCapture(0)

while(True):

    # Capture the video frame by frame
    ret, frame = vid.read()

    ret2, frame2 = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    cv2.imshow('frame2', frame2)
    


    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# after loop release cap object
vid.release()

cv2.destroyAllWindows()