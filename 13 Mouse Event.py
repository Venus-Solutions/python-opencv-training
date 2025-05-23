import cv2

cap = cv2.VideoCapture(1)

def onMouseMove(event, x, y, flags, param):
    if(event == cv2.EVENT_MOUSEMOVE):
        position = str(x) + ", " + str(y)
        cv2.putText(frame, position, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 ,255), cv2.LINE_4)
        cv2.imshow("Live Stream", frame)

while(True):
    success, frame = cap.read()
    cv2.imshow("Live Stream", frame)
    cv2.setMouseCallback("Live Stream", onMouseMove)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()