import cv2
import numpy as np
# Membaca gambar
image = cv2.imread('kucing.jpg')

points1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
points2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

M_perspective = cv2.getPerspectiveTransform(points1, points2)

perspective_transformed_image = cv2.warpPerspective(image, M_perspective, (300, 300))

cv2.imshow('perspective_transformed_image', perspective_transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()