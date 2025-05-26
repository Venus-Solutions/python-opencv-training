import cv2

from picamera2 import Picamera2

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (800, 600)}))
picam2.start()

frame1 = picam2.capture_array()
frame2 = picam2.capture_array()

while True:
    motiondiff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(motiondiff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh, result = cv2.threshold(blur, 15, 255, cv2.THRESH_BINARY)
    dilation = cv2.dilate(result, None, iterations = 3)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame1, contours, -1, (0,255,0), 2)
    cv2.imshow("Output", frame1)
    frame1 = frame2
    frame2 = picam2.capture_array()
    if (cv2.waitKey(1) & 0xFF == ord("q")):
        break

picam2.stop()
cv2.destroyAllWindows()