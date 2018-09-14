import cv2
import cv2.aruco as aruco

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters =  aruco.DetectorParameters_create()
 
    corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    
    frame_detected = aruco.drawDetectedMarkers(frame, corners)
    cv2.imshow('frame',frame_detected)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



