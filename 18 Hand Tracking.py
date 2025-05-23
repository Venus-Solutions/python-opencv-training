import cv2
import mediapipe as mp

cap = cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, frame = cap.read()
    results = hands.process(frame)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = frame.shape
                cv2.putText(frame, str(id), (int(lm.x*w + 5), int(lm.y*h - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
            mpDraw.draw_landmarks(frame, handLms)
    cv2.imshow("Live Stream", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()