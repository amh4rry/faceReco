import cv2 
import numpy as np 
import os 
import csv
from datetime import datetime

#recognizer model load section
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_model.yml")
print("model loaded successfully") 

#attendance csv section
attendance_file = "attendance.csv"

if not os.path.exists(attendance_file):
    with open(attendance_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date", "Time"])


dataset_path = "dataset"
users = os.listdir(dataset_path)

label_map = {}
marked_names = []

for index, user in enumerate(users):
    label_map[index] = user

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

camera = cv2.VideoCapture(0)

while True:

    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )
        face_roi = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(face_roi)
        if confidence < 55:
            name = label_map.get(label, "Unknown")
        else:
            name = "Unknown"
        
        if name != "Unknown" and name not in marked_names:
            now = datetime.now()
            date = now.strftime("%Y-%m-%d")
            time = now.strftime("%H:%M:%S")

            with open(attendance_file, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name, date, time])

            marked_names.append(name)
            print(f"Attendance marked for {name}")

        cv2.putText(
        frame,
        f"{name} ({int(confidence)})",
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2)
        
    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
