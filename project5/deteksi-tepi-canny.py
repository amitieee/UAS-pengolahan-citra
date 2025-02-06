import cv2

#membaca gambar dlm grayscale
image = cv2.imread('kucing.jpg', 0)

#menerapkan deteksi tepi canny
edges = cv2.Canny(image, 100, 200)

#menampilkan hasil
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()