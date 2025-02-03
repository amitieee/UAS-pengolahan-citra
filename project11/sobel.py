import cv2
import numpy as np

image = cv2.imread('anjing.jpg', cv2.IMREAD_GRAYSCALE)

sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5) #sobel X
sobely = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5) #sobel Y

cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y', sobely)
cv2.waitKey()
cv2.destroyAllWindows()