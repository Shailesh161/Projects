# Drowsiness Detection System using Eye Aspect Ratio

This Python script utilizes computer vision techniques to detect drowsiness in real-time by analyzing the eye aspect ratio (EAR) of a person's eyes captured through a webcam feed. When the EAR falls below a certain threshold, indicating that the person's eyes are closing or partially closed for an extended period, an alert is triggered to warn the individual.

## Features

- **Real-time Detection**: Continuously monitors the user's eyes in real-time for signs of drowsiness.
- **Eye Aspect Ratio (EAR)**: Utilizes the EAR metric, a measure of eye openness, to determine drowsiness.
- **Alert System**: Displays an alert message on the screen when drowsiness is detected, warning the individual to stay alert.
- **Cross-platform**: Compatible with most platforms supporting Python and OpenCV.

## Prerequisites

Before running the script, ensure you have the following dependencies installed:

- Python 3.x
- OpenCV (cv2)
- imutils
- dlib
- SciPy


Install the dependencies using pip:

```
pip install opencv-python imutils dlib scipy
```

## Usage

1. **Clone the Repository**: Clone this repository to your local machine.

2. **Download Dlib Model**: Download the pre-trained shape predictor model (`shape_predictor_68_face_landmarks.dat`) from the [Dlib website](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) and place it in the `models` directory.

3. **Run the Script**: Execute the `drowsiness_detection.py` script using Python:

```
python drowsiness_detection.py
```

4. **Monitor Alert**: As the script runs, it continuously monitors your eyes through your webcam feed. If drowsiness is detected, an alert message will be displayed on the screen to warn you.

## Customization

- **Threshold Adjustment**: You can adjust the `thresh` variable to set a different threshold for detecting drowsiness based on your preferences or requirements.
- **Frame Check**: Modify the `frame_check` variable to change the number of consecutive frames where drowsiness must be detected before triggering an alert.

## Contributions

Contributions to this project are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

Stay alert and safe with the Drowsiness Detection System! If you have any feedback or suggestions, please don't hesitate to reach out.
