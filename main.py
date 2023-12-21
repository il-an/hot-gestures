from recognition import GestureRecogniser
from system_interaction import Interact
from time import sleep

gesture_recogniser = GestureRecogniser()
interactor = Interact()

while True:
    # main loop
    event = gesture_recogniser.gesture_tick()
    if event == gesture_recogniser.copy:
        interactor.copy()
    elif event == gesture_recogniser.cut:
        interactor.cut()
    elif event == gesture_recogniser.paste:
        interactor.paste()
    elif event == gesture_recogniser.quit:
        interactor.quit()

    sleep(0.05)  # delay before next event
