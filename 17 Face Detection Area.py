import cv2

cap = cv2.VideoCapture(1)
faceCascade = cv2.CascadeClassifier("*****model file directory*****/haarcascade_frontalface_default.xml")
cx = 0
cy = 0
area = 0
while(True):
    success, frame = cap.read()
    grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faceDetect = faceCascade.detectMultiScale(grayScale)
    for (x, y, w, h) in faceDetect:
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
        if(area > 60000):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
            cv2.putText(frame, str(area) + "px (Too Close)", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif(area < 30000):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 5)
            cv2.putText(frame, str(area) + "px (Too Far)", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        else:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)
            cv2.putText(frame, str(area) + "px", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Live Camera", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()