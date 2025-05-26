import cv2
from picamera2 import Picamera2

print(cv2.__version__)

picam2 = Picamera2()
preview_config = picam2.create_preview_configuration(main={"size": (800, 600)})
picam2.configure(preview_config)
picam2.start()

while(True):
    frame = picam2.capture_array()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('Frame Title', rgb)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

picam2.stop()
cv2.destroyAllWindows()