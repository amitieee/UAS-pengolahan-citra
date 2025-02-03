import cv2
from skimage.feature import greycomatrix, greycoprops

image = cv2.imread('kucing.jpg', 0)
                   
glcm = greycomatrix(image, distance=[1], angles=[0], levels=256, symmetric=True, normed=True)

contrast = greycoprops(glcm, 'contrast')[0, 0]
energy = greycoprops(glcm, 'energy')[0, 0]

print(f'Contrast: {contrast}, Energy: {energy}')