import cv2
print(cv2.getBuildInformation())

orb = cv2.ORB_create()

sift = cv2.SIFT_create()

image = cv2.imread('kucing.jpg')

surf = cv2.xfeatures2d.SURF_create()

keypoints, descriptors = surf.detectAndCompute(image, None)

surf_image = cv2.drawKeypoints(image, keypoints, None)

cv2.imshow('SURF Features', surf_image)
cv2.waitKey(0)
cv2.destroyAllWindows()