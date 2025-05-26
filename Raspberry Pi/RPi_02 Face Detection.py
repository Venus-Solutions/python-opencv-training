import cv2
from picamera2 import Picamera2

face_detector = cv2.CascadeClassifier("/home/pi/Desktop/haarcascade_frontalface_default.xml")
cv2.startWindowThread()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (800, 600)}))
picam2.start()

while True:
    img = picam2.capture_array()

    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(grey, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0),2)

    cv2.imshow("Camera", img)
    cv2.waitKey(1)

picam2.stop()
cv2.destroyAllWindows()