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

fingersPos = []
count = 0
antiCount = True

while True:
    img = picam2.capture_array()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = imgRGB.shape
                if id == 0:
                    fingersPos = []

                fingersPos.append([int(lm.x*w), int(lm.y*h)])
                # cv2.circle(imgRGB, (int(lm.x*w), int(lm.y*h)), 10, (255, 255, 255), cv2.FILLED)
                cv2.putText(imgRGB, str(id), (int(lm.x*w), int(lm.y*h)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
                

            if fingersPos[8][1] > fingersPos[4][1]:
                count = 0
            elif fingersPos[8][1] < fingersPos[6][1]:
                count = 1
                if fingersPos[12][1] < fingersPos[10][1]:
                    count = 2
                    if fingersPos[16][1] < fingersPos[14][1]:
                        count = 3
                        if fingersPos[20][1] < fingersPos[18][1]:
                            count = 4
                            if (fingersPos[4][0] < fingersPos[3][0] and fingersPos[0][0] > fingersPos[1][0]) or (fingersPos[4][0] > fingersPos[3][0] and fingersPos[0][0] < fingersPos[1][0]):
                                count = 5

            cv2.putText(imgRGB, str(count), (w - 200,  h - 50), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 9)

            # mpDraw.draw_landmarks(imgRGB, handLms)
            mpDraw.draw_landmarks(imgRGB, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Live Stream", imgRGB)
    if (cv2.waitKey(1) & 0xFF == ord("q")):
        break

picam2.stop()
cv2.destroyAllWindows()