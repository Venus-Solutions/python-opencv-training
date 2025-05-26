import cv2
import mediapipe as mp
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (800, 600)}))
picam2.start()

mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh()
mpDraw = mp.solutions.drawing_utils
drawSpec = mpDraw.DrawingSpec(thickness = 1, circle_radius=2)

faceLmsPos = []
direction = ""

while True:
    img = picam2.capture_array()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            for id, lm in enumerate(faceLms.landmark):
                h, w, c = img.shape
                # cv2.circle(img, (int(lm.x*w), int(lm.y*h)), 3, (255, 255, 255), cv2.FILLED)
                cv2.putText(img, str(id), (int(lm.x*w), int(lm.y*h)), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (0, 255, 255), 1)

                if id == 0:
                    faceLmsPos = []

                faceLmsPos.append([int(lm.x*w), int(lm.y*h)])
            
            if faceLmsPos[10][0] > faceLmsPos[1][0]:
                direction = "R"
            else: direction = "L"

            mpDraw.draw_landmarks(imgRGB, faceLms, mpFaceMesh.FACEMESH_CONTOURS, drawSpec)
            # cv2.putText(img, direction, (w - 200,  h - 50), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 9)

    cv2.imshow("Live Stream", img)
    if (cv2.waitKey(1) & 0xFF == ord("q")):
        break

picam2.stop()
cv2.destroyAllWindows()