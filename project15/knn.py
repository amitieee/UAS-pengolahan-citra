import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def load_data():
    images = [] #list untuk citra
    labels = [] #list untuk label
    for i in range(1, 3):
        image = cv2.imread(f'image_{i}.jpg', cv2.IMREAD_GRAYSCALE)
        images.append(image.flatten())
        labels.append(i)
    return np.array(images), np.array(labels)

X, y = load_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

accuracy = knn.score(X_test, y_test)
print(f'Akurasi KNN: {accuracy * 100:.2f}%')