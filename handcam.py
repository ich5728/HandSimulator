import cv2
from Undistortion import UndistortFisheye
from PerspectiveTransformation import EagleView


cam = UndistortFisheye("Front_Camera")
frontEagle = EagleView()
frontEagle.setDimensions((186, 195), (484, 207), (588, 402), (97, 363))


handcam = cv2.VideoCapture(0)

while(1):
    ret, frame = handcam.read()
    
    right = cam.undistort(frame)
    
    left = cv2.flip(right, 1)
    
    # fullscreen = cv2.hconcat([left, right])
    two = cv2.hconcat([frame, right])
    
    cv2.namedWindow("hand", cv2.WINDOW_NORMAL)
    cv2.imshow("hand", two)
    key = cv2.waitKey(1) & 0xff
    if key == ord("q"):
        break

cv2.destroyAllWindows()