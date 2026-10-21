import cv2
import numpy as np
import winsound  # For Windows. On Mac/Linux, use print('\a') or playsound library
# 1. Start the webcam (0 is usually the default laptop camera)
cap = cv2.VideoCapture(0)
print("Fire detection system running. Press 'q' to quit.")
while True:
    # Read the current frame from the camera
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break
    # 2. Blur the frame to reduce noise and false positives
    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    # 3. Convert BGR to HSV color space (better for color detection)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    # 4. Define HSV bounds for fire colors (Yellow to Orange)
    lower_fire = np.array([18, 50, 50], dtype=np.uint8)
    upper_fire = np.array([35, 255, 255], dtype=np.uint8)
    # 5. Create mask isolating fire-colored pixels
    mask = cv2.inRange(hsv, lower_fire, upper_fire)
    # 6. Count fire-colored pixels in the mask
    fire_pixels = cv2.countNonZero(mask)
    # 7. Threshold check — trigger alarm if fire pixels exceed limit
    threshold = 15000  # Adjust based on camera resolution
    if fire_pixels > threshold:
        print("FIRE DETECTED! SOUNDING ALARM!")
        winsound.Beep(1000, 500)  # 1000 Hz beep for 500ms
    # 8. Display live feed and fire mask for monitoring/debugging
    cv2.imshow('Live Camera Feed', frame)
    cv2.imshow('Fire Mask (Debugging)', mask)
    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Clean up: release camera and close all windows
cap.release()
cv2.destroyAllWindows()


