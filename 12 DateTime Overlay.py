import cv2
import datetime

cap = cv2.VideoCapture(1)
while(True):
    success, frame = cap.read()
    currentDate = str(datetime.datetime.now())
    cv2.putText(frame, currentDate, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), cv2.LINE_4)
    cv2.imshow("Live Camera", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()