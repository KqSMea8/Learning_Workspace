
import cv2
capture = cv2.VideoCapture('/home/sanjay/Videos/demo1.mp4')
# print(1)

while(capture.isOpened()):
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(30) == ord('q'):
        break