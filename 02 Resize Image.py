import cv2

img = cv2.imread("*****image file directory*****")
img_resize = cv2.resize(img, (500, 500))
cv2.imshow("Output", img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
