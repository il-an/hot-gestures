import pyautogui
import time

pyautogui.PAUSE = 2.5
sleep_time = 0.1


def copy():
    with pyautogui.hold(['command']):
        time.sleep(sleep_time)
        pyautogui.press('c')


def paste():
    with pyautogui.hold(['command']):
        time.sleep(sleep_time)
        pyautogui.press('v')


def cut():
    with pyautogui.hold(['command']):
        time.sleep(sleep_time)
        pyautogui.press('x')


def select_all():
    with pyautogui.hold(['command']):
        time.sleep(sleep_time)
        pyautogui.press('a')


def undo():
    with pyautogui.hold(['command']):
        time.sleep(sleep_time)
        pyautogui.press('z')


def minimize():
    with pyautogui.hold('command'):
        time.sleep(sleep_time)
        pyautogui.press('m')
