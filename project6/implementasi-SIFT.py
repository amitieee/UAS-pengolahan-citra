import cv2

image = cv2.imread('kucing.jpg')

sift = cv2.SIFT_create()

keypoints, descriptors = sift.detectAndCompute(image, None)

sift_image =cv2.drawKeypoints(image, keypoints, None)

cv2.imshow('SIFT Features', sift_image)
cv2.waitKey(0)
cv2.destroyAllWindows()