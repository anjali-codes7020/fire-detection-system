# 🔥 Fire Detection System Using Python & OpenCV

## 📌 Project Description

This project is a simple **Fire Detection System** developed using **Python and OpenCV**. It uses the computer's webcam to detect fire-like colors in real time.

The system converts the camera feed into the **HSV color space** and identifies pixels having colors similar to yellow/orange fire. If the number of detected fire-colored pixels crosses a predefined threshold, the system displays a **"FIRE DETECTED!"** message and sounds an alarm.

---

## 🚀 Features

- 📷 Real-time webcam monitoring
- 🔥 Fire color detection
- 🎨 HSV-based image processing
- 🖼️ Live camera feed display
- 🔍 Fire detection mask for debugging
- 🔊 Alarm using `winsound`
- ⌨️ Press **Q** to stop the program

---

## 🛠️ Technologies Used

- **Python**
- **OpenCV**
- **NumPy**
- **Webcam**
- **winsound** (Windows)

---

## 📋 Requirements

Make sure Python is installed on your computer.

Install the required libraries using:

```bash
pip install opencv-python numpy
```

> `winsound` is included with Python on Windows, so it normally does not need to be installed separately.

---

## 📂 Project Structure

```text
Fire-Detection-System/
│
├── fire_detection.py
└── README.md
```

---

## ▶️ How to Run

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project Folder

```bash
cd Fire-Detection-System
```

### Step 3: Install Required Libraries

```bash
pip install opencv-python numpy
```

### Step 4: Run the Program

```bash
python fire_detection.py
```

---

## 🔥 How It Works

The system follows these steps:

1. Opens the computer's webcam.
2. Captures video frames continuously.
3. Applies Gaussian Blur to reduce image noise.
4. Converts the frame from **BGR to HSV**.
5. Defines HSV values for fire-like colors.
6. Creates a mask containing detected fire-colored pixels.
7. Counts the detected pixels.
8. Compares the pixel count with a predefined threshold.
9. If the number is greater than the threshold:
   - Displays `FIRE DETECTED!`
   - Produces an alarm sound.
10. Press **Q** to exit.

---

## ⚙️ Fire Detection Threshold

The program uses:

```python
threshold = 15000
```

If the number of fire-colored pixels is greater than `15000`, the alarm is triggered.

You can adjust this value depending on your camera resolution and environment.

---

## ⚠️ Limitations

This is a **basic color-based fire detection system**. It may produce false detections when it sees objects with colors similar to fire, such as:

- 🟠 Orange objects
- 🟡 Yellow objects
- 💡 Bright lights
- 🌅 Certain backgrounds

For more accurate detection, a machine-learning or deep-learning model such as **YOLO** can be used.

---

## 💻 Operating System

The current version is designed primarily for **Windows** because it uses:

```python
import winsound
```

For Linux or macOS, the alarm mechanism should be replaced with another audio library or system sound.

---

## 🎯 Future Improvements

- Use YOLO for accurate fire detection
- Add smoke detection
- Add email/SMS notifications
- Add video recording when fire is detected
- Improve false-positive handling
- Create a graphical user interface
- Add cloud monitoring
- Support multiple cameras

---

## 👩‍💻 Author

**Anjali Deshmukh**

---

## 📜 License

This project is created for **educational and learning purposes**.