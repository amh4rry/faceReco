import os
import cv2
import time
img_count = 0
max_images = 20

face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml")

dataset_path = "dataset"

if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)
    print("Dataset folder created")
else:
    print("Dataset folder already exists")

user_name = input("Enter your name: ").strip()

user_path = os.path.join(dataset_path, user_name)

if not os.path.exists(user_path):
    os.makedirs(user_path)
    print(f"Folder created for user: {user_name}")
else:
    print("User folder already exists")


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
        cv2.imshow("Cropped Face", face_roi)
        if img_count < max_images:
            img_name = f"{user_name}_{img_count}.jpg"
            img_path = os.path.join(user_path, img_name)

            cv2.imwrite(img_path, face_roi)
            img_count += 1

            print(f"Saved image {img_count}/{max_images}")
        time.sleep(1)
        



    cv2.imshow("Face Registration - Camera Check", frame)

    if img_count >= max_images:
        print("Face registration completed")
        break

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
