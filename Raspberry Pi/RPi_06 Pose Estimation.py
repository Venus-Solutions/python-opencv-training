import cv2
import mediapipe as mp
import math
import numpy as np
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XBGR8888', "size": (800, 600)}))
picam2.start()

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils
drawSpec = mpDraw.DrawingSpec(thickness = 1, circle_radius=2)

faceLmsPos = []
direction = ""

while True:
    img = picam2.capture_array()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    
    if results.pose_landmarks:
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = imgRGB.shape
            cv2.circle(imgRGB, (int(lm.x*w), int(lm.y*h)), 3, (255, 255, 255), cv2.FILLED)
            cv2.putText(imgRGB, str(id), (int(lm.x*w), int(lm.y*h)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

            if id == 0:
                poseLmsPos = []

            poseLmsPos.append([int(lm.x*w), int(lm.y*h)])
            
        # if poseLmsPos[19][1] < poseLmsPos[10][1]:
        #     direction = "Up"
        # else: direction = "Down"

        angle = math.degrees(math.atan2(poseLmsPos[15][1] - poseLmsPos[13][1], poseLmsPos[15][0] - poseLmsPos[13][0]) - 
                             math.atan2(poseLmsPos[11][1] - poseLmsPos[13][1], poseLmsPos[11][0] - poseLmsPos[13][0]))

        percent = np.interp(angle, (20, 70), (100, 0))
        bar = np.interp(percent, (0, 100), (0, h))
        mpDraw.draw_landmarks(imgRGB, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        cv2.putText(imgRGB, str(percent), (w - 250,  h - 50), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 255, 0), 6)
        cv2.rectangle(imgRGB, (0, h), (50, h - int(bar)), (0, 0, 255), cv2.FILLED)

    cv2.imshow("Live Stream", imgRGB)
    if (cv2.waitKey(1) & 0xFF == ord("q")):
        break

picam2.stop()
cv2.destroyAllWindows()