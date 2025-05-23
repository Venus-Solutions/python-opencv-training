import cv2

cap = cv2.VideoCapture(1)
faceCascade = cv2.CascadeClassifier("*****model file directory*****/haarcascade_frontalface_default.xml")
while(True):
    success, frame = cap.read()
    grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faceDetect = faceCascade.detectMultiScale(grayScale)
    for (x, y, w, h) in faceDetect:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)
    cv2.imshow("Live Camera", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()