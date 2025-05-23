import cv2

cap = cv2.VideoCapture(1)
while(True):
    success, frame = cap.read()
    cv2.putText(frame, "OpenCV", (150, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), cv2.LINE_4)
    cv2.putText(frame, "OpenCV", (150, 250), cv2.FONT_HERSHEY_TRIPLEX, 2.5, (0, 255, 0), cv2.LINE_4)
    cv2.putText(frame, "OpenCV", (150, 350), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), cv2.LINE_8)
    cv2.imshow("Live Camera", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()