import pyautogui
import time
import platform

sleep_time = 0.1


class Interact:

    def __init__(self):
        if platform.system() == "Darwin":
            self.key = "command"
        else:
            self.key = "ctrl"

    def copy(self):
        with pyautogui.hold([self.key]):
            time.sleep(sleep_time)
            pyautogui.press('c')

    def paste(self):
        with pyautogui.hold([self.key]):
            time.sleep(sleep_time)
            pyautogui.press('v')

    def cut(self):
        with pyautogui.hold([self.key]):
            time.sleep(sleep_time)
            pyautogui.press('x')

    def select_all(self):
        with pyautogui.hold([self.key]):
            time.sleep(sleep_time)
            pyautogui.press('a')

    def undo(self):
        with pyautogui.hold([self.key]):
            time.sleep(sleep_time)
            pyautogui.press('z')

    def minimize(self):
        with pyautogui.hold(self.key):
            time.sleep(sleep_time)
            pyautogui.press('m')
