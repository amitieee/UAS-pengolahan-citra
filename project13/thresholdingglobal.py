import cv2
import numpy as np

image = cv2.imread('kucing.jpg', cv2.IMREAD_GRAYSCALE)

ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Thresholded Image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()