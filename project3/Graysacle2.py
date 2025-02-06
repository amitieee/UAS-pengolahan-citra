import cv2

# Membaca gambar RGB
image_rgb = cv2.imread('kucing.jpg')

# Konversi gambar ke Grayscale
image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)

# Menyimpan atau menampilkan hasil gambar Grayscale
cv2.imshow('Grayscale Image', image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
