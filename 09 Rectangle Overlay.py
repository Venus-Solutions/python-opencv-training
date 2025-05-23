import cv2

cap = cv2.VideoCapture(1)
while(True):
    success, frame = cap.read()
    cv2.rectangle(frame, (0, 0), (400, 400), (0, 255, 0), 5)
    cv2.rectangle(frame, (100, 100), (400, 400), (0, 0, 255), 3)
    cv2.rectangle(frame, (300, 200), (600, 450), (255, 255, 0), -1)
    cv2.imshow("Live Camera", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
