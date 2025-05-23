import cv2

img = cv2.imread("*****image file directory*****")
cv2.imshow("Output", img)
cv2.waitKey(5000)
cv2.destroyAllWindows()