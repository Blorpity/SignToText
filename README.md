# SignToText

**SignToText** is an application that translates **American Sign Language (ASL)** gestures into text in real time.  
The translated text is written to a `.txt` file for further use or integration.  
Currently, the project focuses on recognizing **ASL alphabet gestures**, with plans to expand to full word and phrase detection.
An option to run the application as a browser extension will also be added.

---

## Overview

SignToText uses **computer vision** and **machine learning** to interpret hand gestures captured through a live camera feed.  
By leveraging **TensorFlow**, **OpenCV**, and **MediaPipe**, the system detects hand landmarks, interprets gestures, and outputs corresponding text.

---

## Tech Stack

- **Python**
- **TensorFlow**
- **OpenCV**
- **MediaPipe**
- **NumPy**

---

## Setup & Installation

> **Note:** Setup instructions are currently **TBD**.  
> This section will be updated as the project matures and installation requirements are finalized.

---

## Usage

1. Run the application.  
2. Allow access to your system camera.  
3. Perform ASL gestures in front of the camera.  
4. The recognized letter will be:
   - Displayed in a defined text bar
   - Saved to a `.txt` file for output.

---

## Features

- Real-time ASL alphabet recognition  
- Hand tracking using MediaPipe  
- Gesture-to-text output  
- Continuous I/O stream handling  
- Expandable architecture for additional signs and words  

---

## Roadmap

- [ ] Complete alphabet recognition  
- [ ] Add support for common words and phrases  
- [ ] Integrate GUI for user-friendly interaction  
- [ ] Improve model accuracy and robustness  

---

## Contributing

Contributions, issues, and feature requests are welcome.  
Feel free to contact me at tonatiuhula8@gmail.com

---

## Acknowledgments

- [MediaPipe](https://github.com/google/mediapipe) for hand-tracking models  
- [TensorFlow](https://www.tensorflow.org/) for machine learning tools  
- [OpenCV](https://opencv.org/) for real-time image processing  

---

> *SignToText is an ongoing project. Early-stage development focuses on building accurate gesture recognition and a reliable text output pipeline.*
