import cv2
import numpy as np

image = cv2.imread('jack.jpg', cv2.IMREAD_GRAYSCALE)

gray = np.float32(image)
corners = cv2.cornerHarris(gray, 2, 3, 0.04)

color_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
color_image[corners > 0.01 * corners.max()] = [0, 0, 255]

cv2.imshow('Harris Corner Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()