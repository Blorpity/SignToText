import mediapipe as mp
import cv2
import pandas as pd
import tensorflow as tf
import numpy as np
from PIL import Image

from google.protobuf.json_format import MessageToDict

print("Mediapipe version:", mp.__version__)
print("OpenCV version:", cv2.__version__)

model_path = r"C:\Users\tonat\OneDrive\Documents\GitHub\SignToText\ASL.h5\ASL.h5"
model = tf.keras.models.load_model(model_path)

print("Model loaded successfully")
print("Model SUmmary:")
model.summary()

def initialization():
    # Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands = 1)
    mp_drawing = mp.solutions.drawing_utils
    
    # Webcam
    cam = cv2.VideoCapture(0)

    # ASL dataset
    dataset = None

    return mp_hands, hands, mp_drawing, cam, dataset

def processing(mp_hands, hands, mp_drawing, cam, dataset):
    while cam.isOpened():
        success, img = cam.read()
        if not success:
            print("Empty Camera. Ignoring it...")
            continue

        # Convert the BGR image to RGB
        img = cv2.flip(img, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img)

        # Convert back to BGR for OpenCV display
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            if len(results.multi_handedness) > 1:
                cv2.putText(img, 'Multiple Hands', (210, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
            else:
                for i in results.multi_handedness:
                    leftOrRight = MessageToDict(i)['classification'][0]['label']

                    if leftOrRight == 'Left':
                        cv2.putText(img, "Left Hand", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
                    
                    if leftOrRight == 'Right':
                        cv2.putText(img, "Right Hand", (450, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)


        cv2.imshow('MediaPipe Hands', img)
        if (cv2.waitKey(5) & 0xFF == 27) or (cv2.getWindowProperty('MediaPipe Hands', cv2.WND_PROP_VISIBLE) < 1):
            break

    cam.release()
    cv2.destroyAllWindows()

def main():
    print("Starting SignToText...")



    # mp_hands, hands, mp_drawing, cam, dataset = initialization()
    # processing(mp_hands, hands, mp_drawing, cam, dataset)
    


if __name__ == "__main__":
    main()

