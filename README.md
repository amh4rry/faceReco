# 🎯 Face Recognition Attendance System

A real-time Face Recognition based Attendance System built using Python and OpenCV (LBPH Algorithm).

This project detects faces from a live camera feed, recognizes registered users, and automatically marks attendance in a CSV file while preventing duplicate entries per session.

---

## 🚀 Features

- ✅ Face Detection using Haar Cascade
- ✅ Face Registration (Multi-user Support)
- ✅ Model Training using LBPH Face Recognizer
- ✅ Live Face Recognition
- ✅ Unknown Face Filtering (Confidence Threshold)
- ✅ Attendance Logging (CSV)
- ✅ Duplicate Prevention per Session

---

## 🧠 Technologies Used

- Python 3.10 / 3.11 (Recommended)
- OpenCV (opencv-contrib-python)
- NumPy
- CSV (for attendance storage)

---

## 📁 Project Structure

```
faceReco/
│
├── dataset/                  # Registered users' face images
│   ├── User1/
│   ├── User2/
│   └── ...
│
├── face_registration.py      # Capture and store face samples
├── train_model.py            # Train LBPH model
├── recognize_face.py         # Live recognition + attendance logging
├── face_model.yml            # Trained model file
├── attendance.csv            # Attendance records
└── haarcascade_frontalface_default.xml
```

---

## 🛠 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/face-recognition-attendance.git
cd face-recognition-attendance
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install opencv-contrib-python numpy
```

⚠️ Important: Use Python 3.10 or 3.11 for compatibility with OpenCV face module.

---

## 📸 How to Use

### Step 1 – Register a New User

```bash
python face_registration.py
```

- Enter the user's name
- System captures 20 face images
- Images are saved in `dataset/username/`

---

### Step 2 – Train the Model

```bash
python train_model.py
```

- Reads all registered users
- Assigns numeric labels automatically
- Trains LBPH face recognizer
- Saves trained model as `face_model.yml`

---

### Step 3 – Start Attendance System

```bash
python recognize_face.py
```

- Opens live webcam
- Detects and recognizes faces
- Marks attendance in `attendance.csv`
- Prevents duplicate entries per session

---

## 📊 Attendance File Format

Example (`attendance.csv`):

```
Name,Date,Time
Harsh,2026-02-22,10:41:23
Aman,2026-02-22,10:43:11
```

---

## 🔐 Recognition Logic

- Uses LBPH Face Recognizer
- Confidence threshold applied
- Lower confidence value = better match
- Faces above threshold are marked as "Unknown"

Example threshold setting:

```python
THRESHOLD = 55
```

Lower value → stricter recognition  
Higher value → more flexible recognition  

---

## 🔄 Workflow Summary

1. Capture face samples
2. Train model
3. Recognize users in real-time
4. Log attendance automatically

---

## 🚧 Future Improvements

- Daily attendance restriction
- Punch In / Punch Out system
- GUI interface (Tkinter / PyQt)
- Web-based version (Flask / Django)
- Anti-spoofing (Blink detection)
- Database integration (MySQL / SQLite)

---

## 🎓 Learning Outcomes

This project demonstrates:

- Computer Vision fundamentals
- Face Detection & Recognition
- Dataset creation and labeling
- Model training using LBPH
- Real-time video processing
- File handling and state management

---

## 👤 Author

Harsh Sharma  
Aspiring Generative AI Developer  

---

## 📜 License

This project is open-source and free to use for educational purposes.
