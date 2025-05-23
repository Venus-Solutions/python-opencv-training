import cv2

cap = cv2.VideoCapture(1)
while(True):
    success, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.imshow("Live Camera Gray", gray)
    cv2.imshow("Live Camera BGR", bgr)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()