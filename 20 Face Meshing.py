import cv2
import mediapipe as mp

cap = cv2.VideoCapture(1)

mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh()
mpDraw = mp.solutions.drawing_utils
drawSpec = mpDraw.DrawingSpec(thickness = 1, circle_radius = 1)

while True:
    success, frame = cap.read()
    results = faceMesh.process(frame)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            for id, lm in enumerate(faceLms.landmark):
                h, w, c = frame.shape
                # cv2.putText(frame, str(id), (int(lm.x*w), int(lm.y*h)), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (0, 255, 255), 1)
    mpDraw.draw_landmarks(frame, faceLms, mpFaceMesh.FACEMESH_CONTOURS, drawSpec)
    cv2.imshow("Live Stream", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()