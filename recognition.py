import cv2
import mediapipe as mp
import numpy as np
import time
from gestures import copy
from gestures import cut
from gestures import paste
from gestures import quit


class GestureRecogniser:
    """Recognizes gestures and returns their codes"""

    def __init__(self):
        # initializes the recognizer

        # gesture codes
        self.copy = 0
        self.cut = 1
        self.paste = 2
        self.quit = 3

        # time before recognition of another gesture
        self.IGNORE_TIME = 2

        self.last_gesture_time = time.time()
        self.detector = mp.solutions.hands.Hands()
        self.cap = cv2.VideoCapture(0)

    def get_camera_image(self):
        # returns image from camera
        ret, frame = self.cap.read()
        if not ret:
            return None
        frame = np.fliplr(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame

    def get_hands(self, img):
        # returns hands from image
        return self.detector.process(img)

    def get_camera_hands(self):
        # returns hands from camera
        return self.get_hands(self.get_camera_image())

    def gesture_tick(self):
        # returns code of recognized gesture
        hands = self.get_camera_hands()
        if hands.multi_hand_landmarks is None:
            return

        ctime = time.time()

        if ctime - self.last_gesture_time < self.IGNORE_TIME:
            return None

        for i in range(len(hands.multi_hand_landmarks)):
            args = [hands.multi_hand_landmarks[i].landmark,
                    hands.multi_handedness[i].classification[0].label]
            if copy.gesture_copy(hands.multi_hand_landmarks[i].landmark):
                self.last_gesture_time = time.time()
                return self.copy
            if cut.gesture_cut(hands.multi_hand_landmarks[i].landmark):
                self.last_gesture_time = time.time()
                return self.cut
            if paste.gesture_paste(hands.multi_hand_landmarks[i].landmark):
                self.last_gesture_time = time.time()
                return self.paste
            if quit.gesture_quit(hands.multi_hand_landmarks[i].landmark,
                                 hands.multi_handedness[i].classification[0].label):
                self.last_gesture_time = time.time()
                return self.quit
        return None
