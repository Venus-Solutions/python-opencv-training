import cv2
import numpy

cap = cv2.VideoCapture(1)

def onMouseMove(event, x, y, flags, param):
    if(event == cv2.EVENT_MOUSEMOVE):
        blue = frame[y, x, 0]
        green = frame[y, x, 1]
        red = frame[y, x, 2]
        # position = str(red) + ", " + str(green) + ", " + str(blue)
        # cv2.putText(frame, position, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 ,255), cv2.LINE_4)
        frameColor = numpy.zeros([500, 500, 3], numpy.uint8)
        frameColor[:] = [blue, green, red]
        cv2.imshow("Color Picker", frameColor)

while(True):
    success, frame = cap.read()
    cv2.imshow("Live Stream", frame)
    cv2.setMouseCallback("Live Stream", onMouseMove)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()