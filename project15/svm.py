import cv2
import numpy as np
import sklearn 
import svm
from sklearn.model_selection import train_test_split

def load_data():
    images = [] #list untuk citra
    labels = [] #list untuk label
    for i in range(1, 3): #misalnya, 10 citra
        image = cv2.imread(f'image_{i}.jpg', cv2.IMREAD_GRAYSCALE)
        images.append(image.flatten()) #ubah citra menjadi vektor 1D
    return np.array(images), np.array(labels)

X, y = load_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = svm.SVC(kernel='linear')
model.fit(X_train, y_train)

accuracy = model.score(X_train, y_train)
print(f'Akurasi SVM: {accuracy * 100:.2f}%')