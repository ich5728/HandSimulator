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
    
    fullscreen = cv2.hconcat([right, left])
    
    
    cv2.namedWindow("hand", cv2.WINDOW_NORMAL)
    cv2.imshow("hand", fullscreen)
    key = cv2.waitKey(1) & 0xff
    if key == ord("q"):
        break

cv2.destroyAllWindows()