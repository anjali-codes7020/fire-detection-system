\# 🔥 Fire Detection System Using Python and OpenCV



A simple real-time \*\*fire-color detection system\*\* built with Python, OpenCV, NumPy, and the Windows `winsound` module.



\## Project Overview



The program uses a webcam to capture live video, converts frames to HSV color space, detects yellow/orange fire-like regions, counts the detected pixels, and activates an audible alarm when the number of detected pixels exceeds a threshold.



> \*\*Important:\*\* This is an educational computer-vision prototype, not a certified fire-safety system.



\## Technologies Used



\- Python 3.x

\- OpenCV (`cv2`)

\- NumPy

\- Windows `winsound`

\- Webcam



\## Project Structure



```text

Fire-Detection-System/

│

├── fire\_detection.py

└── README.md

```



\## Requirements



\- Windows

\- Python 3.x

\- Laptop or USB webcam



\## Installation



\### 1. Check Python



```bash

python --version

```



\### 2. Install OpenCV



```bash

pip install opencv-python

```



\### 3. Install NumPy



```bash

pip install numpy

```



\### 4. Verify OpenCV



```bash

python -c "import cv2; print(cv2.\_\_version\_\_)"

```



\## How to Run



Save your code as:



```text

fire\_detection.py

```



Then open Command Prompt in that folder and run:



```bash

python fire\_detection.py

```



The program displays:



\- \*\*Live Camera Feed\*\*

\- \*\*Fire Mask (Debugging)\*\*



Press \*\*`q`\*\* while the camera window is active to stop the program.



\## How It Works



```text

Webcam

&#x20;  ↓

Capture Frame

&#x20;  ↓

Gaussian Blur

&#x20;  ↓

Convert BGR → HSV

&#x20;  ↓

Select Fire-Color Range

&#x20;  ↓

Create Mask

&#x20;  ↓

Count Fire-Colored Pixels

&#x20;  ↓

Compare With Threshold

&#x20;  ↓

Alarm

```



\### 1. Start the Webcam



```python

cap = cv2.VideoCapture(0)

```



`0` normally selects the default camera. If necessary, try `1` for another camera.



\### 2. Reduce Noise



```python

blur = cv2.GaussianBlur(frame, (21, 21), 0)

```



\### 3. Convert to HSV



```python

hsv = cv2.cvtColor(blur, cv2.COLOR\_BGR2HSV)

```



HSV makes color-based segmentation easier.



\### 4. Define the Fire-Color Range



```python

lower\_fire = np.array(\[18, 50, 50], dtype=np.uint8)

upper\_fire = np.array(\[35, 255, 255], dtype=np.uint8)

```



This approximately targets yellow/orange regions.



\### 5. Create the Mask



```python

mask = cv2.inRange(hsv, lower\_fire, upper\_fire)

```



\### 6. Count Detected Pixels



```python

fire\_pixels = cv2.countNonZero(mask)

```



\### 7. Trigger the Alarm



The current threshold is:



```python

threshold = 15000

```



If the number of detected pixels is greater than the threshold:



```python

winsound.Beep(1000, 500)

```



is used to generate an audible Windows beep.



\## Adjusting the Threshold



The threshold depends on camera resolution and lighting.



Current value:



```python

threshold = 15000

```



If you get too many false alarms, try a larger value:



```python

threshold = 25000

```



If detection is too insensitive, try a smaller value:



```python

threshold = 10000

```



Only test with safe simulated conditions, not an actual fire.



\## Limitations



Because this version primarily detects \*\*color\*\*, it can produce false positives from:



\- Orange/yellow clothing

\- Lamps

\- Sunlight

\- Bright lights

\- Orange objects

\- Reflections



It can also miss a real fire when:



\- The flame is small

\- Lighting is poor

\- The camera is too far away

\- The flame is obscured

\- Its colors fall outside the selected HSV range



Therefore, this system should \*\*not be used as the only fire-safety mechanism\*\*.



\## Future Improvements



For a stronger final-year project, you can add:



1\. YOLO-based fire detection

2\. CNN/deep-learning classification

3\. Smoke detection

4\. Flame + smoke detection

5\. Confidence score

6\. Multiple-camera support

7\. Detection history

8\. MongoDB database

9\. Web dashboard

10\. Email/SMS/mobile alerts

11\. Automatic event recording

12\. False-alarm reduction using detection across multiple frames



\## Safe Testing



Do not intentionally create a real fire for testing.



Use safe test cases such as:



\- Orange/yellow images on a screen

\- Printed orange/yellow objects

\- Synthetic test images



\## Safety Note



This project is for \*\*educational purposes and computer-vision learning\*\*. It does not replace certified smoke detectors, fire alarms, fire suppression equipment, or professional emergency systems.



\## Author : Anjali Patange



\*\*Student Project\*\*



\*\*Project Type:\*\* Computer Vision / Python Mini Project



\*\*Technologies:\*\* Python + OpenCV + NumPy



\## License



Provided for educational purposes.



