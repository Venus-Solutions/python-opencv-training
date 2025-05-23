import cv2

cap = cv2.VideoCapture(1)
while(True):
    success, frame = cap.read()
    cv2.line(frame, (0, 0), (300, 300), (0, 255, 0), 5)
    cv2.line(frame, (50, 100), (400, 200), (0, 255, 255), 5)
    cv2.arrowedLine(frame, (50, 100), (50, 300), (0, 0, 255), 5)
    cv2.imshow("Live Camera", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
