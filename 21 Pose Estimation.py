import cv2
import mediapipe as mp
import math
import numpy as np

cap = cv2.VideoCapture(1)

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

while True:
    success, frame = cap.read()
    results = pose.process(frame)
    
    if results.pose_landmarks:
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = frame.shape
            cv2.putText(frame, str(id), (int(lm.x*w), int(lm.y*h)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
            if id == 0:
                poseLmsPos = []
            poseLmsPos.append([int(lm.x*w), int(lm.y*h)])

        angle = math.degrees(math.atan2(poseLmsPos[15][1] - poseLmsPos[13][1], poseLmsPos[15][0] - poseLmsPos[13][0]) - 
                             math.atan2(poseLmsPos[11][1] - poseLmsPos[13][1], poseLmsPos[11][0] - poseLmsPos[13][0]))
        percent = np.interp(angle, (20, 70), (100, 0))
        bar = np.interp(percent, (0, 100), (0, h))
        cv2.putText(frame, str(percent), (w - 250,  h - 50), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 255, 0), 6)
        cv2.rectangle(frame, (0, h), (50, h - int(bar)), (0, 0, 255), cv2.FILLED)

        mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
    cv2.imshow("Live Stream", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()