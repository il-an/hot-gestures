import mediapipe as mp
from gestures.tools.thumbs_somewhere import is_thumbs_somewhere

lm = mp.solutions.hands.HandLandmark


def gesture_copy(gesture):
    # check if gesture is copy
    ok_thumb = gesture[lm.THUMB_TIP].y < gesture[lm.WRIST].y
    return is_thumbs_somewhere(gesture) and ok_thumb
