import cv2

cam = cv2.VideoCapture(0)

while True:
    rat, frame = cam.read()
    cv2.imshow('test', frame)
    cv2.waitKey(1)
    