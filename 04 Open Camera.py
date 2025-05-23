import cv2

cap = cv2.VideoCapture(1)
while(True):
    success, frame = cap.read()
    cv2.imshow("Live Camera", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()