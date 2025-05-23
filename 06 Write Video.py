import cv2

cap = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
result = cv2.VideoWriter("*****new video file directory*****", fourcc, 20.0, (640, 480))
while(True):
    success, frame = cap.read()
    cv2.imshow("Live Camera", frame)
    result.write(frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

result.release()
cap.release()
cv2.destroyAllWindows()