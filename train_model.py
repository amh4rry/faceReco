import os 
import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()

dataset_path = "dataset"

faces = []
labels = []

users = os.listdir(dataset_path)

label_map = {}

for index,user in enumerate(users):
    label_map[index] = user
    print(f"Label {index} assigned to {user}")

for index, user in enumerate(users):
    user_path = os.path.join(dataset_path, user)

    for img_name in os.listdir(user_path):
        img_path = os.path.join(user_path, img_name)

        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        faces.append(img)
        labels.append(index)

print("Total face images:", len(faces))
print("Total labels:", len(labels))

labels = np.array(labels)
recognizer.train(faces, labels)
print("Model training completed")

recognizer.save("face_model.yml")
print("Model saved successfully")