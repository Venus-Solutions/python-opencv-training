import cv2
import mediapipe as mp

cap = cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

fingersPos = []
count = 0

while True:
    success, frame = cap.read()
    results = hands.process(frame)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = frame.shape
                #Clear fingersPos[]
                if id == 0:
                    fingersPos = []
                fingersPos.append([int(lm.x*w), int(lm.y*h)])
                cv2.putText(frame, str(id), (int(lm.x*w + 5), int(lm.y*h - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
            # if fingersPos[0][0] > fingersPos[1][0]:
            #     cv2.putText(frame, "LEFT", (w - 200,  h - 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
            # else:
            #     cv2.putText(frame, "RIGHT", (w - 200,  h - 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
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

            cv2.putText(frame, str(count), (w - 200,  h - 50), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 9)
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
    cv2.imshow("Live Stream", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()