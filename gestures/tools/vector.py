import numpy as np
import math

# constants
SMALL_ANGLE = 15
VERY_BIG_ANGLE = 140


def get_norm_vector(vector):
    # get normalized vector
    return vector / np.linalg.norm(vector)


def get_angle(v1, v2):
    # get angle between two vectors
    v1, v2 = get_norm_vector(v1), get_norm_vector(v2)
    return np.arccos(np.clip(np.dot(v1, v2), -1.0, 1.0))


def get_angle_deg(v1, v2):
    # get angle between two vectors in degrees
    return get_angle(v1, v2) * (180 / math.pi)


def get_vector(landmarks, i1, i2):
    # get vector between two landmarks
    return np.array([landmarks[i1].x - landmarks[i2].x, landmarks[i1].y - landmarks[i2].y])


def is_small_angle(v1, v2):
    # check if angle between two vectors is small
    return abs(get_angle_deg(v1, v2)) < SMALL_ANGLE


def is_big_angle(v1, v2):
    # check if angle between two vectors is big
    return abs(get_angle_deg(v1, v2)) > SMALL_ANGLE


def is_very_big_angle(v1, v2):
    # check if angle between two vectors is very big
    return abs(get_angle_deg(v1, v2)) > VERY_BIG_ANGLE
