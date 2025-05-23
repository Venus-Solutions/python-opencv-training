import cv2
import numpy

cap = cv2.VideoCapture(1)

def onMouseClick(event, x, y, flags, param):
    if(event == cv2.EVENT_LBUTTONUP):
        blue = frame[y, x, 0]
        green = frame[y, x, 1]
        red = frame[y, x, 2]
        position = str(blue) + ", " + str(green) + ", " + str(red)
        print(position)

while(True):
    success, frame = cap.read()
    lower = numpy.array([58, 65, 91])
    upper = numpy.array([109, 116, 165])
    mask = cv2.inRange(frame, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("Live Stream", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)
    cv2.setMouseCallback("Live Stream", onMouseClick)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()