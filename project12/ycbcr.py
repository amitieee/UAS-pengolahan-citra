import cv2

image = cv2.imread('kucing.jpg')

ycbcr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

Y_channel = ycbcr_image[:,:,0]

cv2.imshow('Y Channel', Y_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()