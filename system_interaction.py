import pyautogui
import time
import platform


class Interact:
    """Interacts with the system"""
    def __init__(self):
        # initializes the sleep time and shortcut key based on OS
        self.sleep_time = 0.1
        if platform.system() == "Darwin":
            self.key = "command"
        else:
            self.key = "ctrl"

    def copy(self):
        # copies the selected text
        with pyautogui.hold([self.key]):
            time.sleep(self.sleep_time)
            pyautogui.press('c')

    def paste(self):
        # pastes the copied text
        with pyautogui.hold([self.key]):
            time.sleep(self.sleep_time)
            pyautogui.press('v')

    def cut(self):
        # cuts the selected text
        with pyautogui.hold([self.key]):
            time.sleep(self.sleep_time)
            pyautogui.press('x')

    def quit(self):
        # quits the current application
        if platform.system() == 'Darwin':
            with pyautogui.hold(self.key):
                time.sleep(self.sleep_time)
                pyautogui.press('q')
        else:
            with pyautogui.hold('alt'):
                time.sleep(self.sleep_time)
                pyautogui.press('f4')
