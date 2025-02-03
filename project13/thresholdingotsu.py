import cv2

image = cv2.imread('kucing.jpg', cv2.IMREAD_GRAYSCALE)

ret, otsu_thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('Otsu Threshold', otsu_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()