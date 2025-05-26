import cv2
import mediapipe as mp
import math
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XBGR8888', "size": (800, 600)}))
picam2.start()

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

x1, y1, x2, y2, length, count = 0, 0, 0, 0, 0, 0
antiCount = True

while True:
    img = picam2.capture_array()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = imgRGB.shape
                if id == 4:
                    # print(id, lm.x*w, lm.y*h)
                    x1, y1 = int(lm.x*w), int(lm.y*h)
                    cv2.circle(imgRGB, (int(lm.x*w), int(lm.y*h)), 15, (255, 0, 0), cv2.FILLED)
                if id == 8:
                    # print(id, lm.x*w, lm.y*h)
                    x2, y2 = int(lm.x*w), int(lm.y*h)
                    cv2.circle(imgRGB, (int(lm.x*w), int(lm.y*h)), 15, (255, 0, 0), cv2.FILLED)

                cv2.line(imgRGB, (x1, y1), (x2, y2), (255, 0, 0), 3)
                length = math.hypot(x2 - x1, y2 - y1)
                cv2.putText(imgRGB, str(int(length)), (w - 80,  50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                if int(length) > 80:
                    antiCount = False
                elif int(length) < 30 and antiCount == False:
                    count = count + 1
                    antiCount = True
                elif y1 < y2:
                    count = 0

                cv2.putText(imgRGB, str(count), (w - 200,  h - 50), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 9)

            # mpDraw.draw_landmarks(imgRGB, handLms)
            mpDraw.draw_landmarks(imgRGB, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Live Stream", imgRGB)
    if (cv2.waitKey(1) & 0xFF == ord("q")):
        break

picam2.stop()
cv2.destroyAllWindows()