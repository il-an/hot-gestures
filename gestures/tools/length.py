import math


def is_length_normal(finger1, finger2, finger3, finger4, length):
    # check if the length of 4 fingers is okay
    return (
            math.hypot(finger1[0], finger1[1]) > length
            and math.hypot(finger2[0], finger2[1]) > length
            and math.hypot(finger3[0], finger3[1]) > length
            and math.hypot(finger4[0], finger4[1]) > length
    )


def is_length_normal_one(finger, length):
    # check if the length of 1 finger is more than minimum
    return (
            math.hypot(finger[0], finger[1]) > length
    )


def is_length_normal_max(finger1, finger2, finger3, finger4, length):
    # check if the length of 4 fingers is less than maximum
    return (
            math.hypot(finger1[0], finger1[1]) < length
            and math.hypot(finger2[0], finger2[1]) < length
            and math.hypot(finger3[0], finger3[1]) < length
            and math.hypot(finger4[0], finger4[1]) < length
    )
