import cv2

cap = cv2.VideoCapture(1)
while(True):
    success, frame = cap.read()
    cv2.circle(frame, (100, 100), 50, (0, 255, 0), 5)
    cv2.circle(frame, (200, 300), 100, (0, 255, 255), 5)
    cv2.circle(frame, (400, 200), 150, (255, 0, 0), -1)
    cv2.imshow("Live Camera", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()