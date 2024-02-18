import random
import time
import pyautogui._pyautogui_win as platformModule


def real_press(key):
    """
    模拟真实按键
    :param key: 按键
    :return:
    """
    platformModule._keyDown(key)
    time.sleep(random.uniform(0.03, 0.07))
    platformModule._keyUp(key)


def real_write(text):
    """
    模拟真实的输入
    :param text: 文本
    :return:
    """
    for char in text:
        real_press(char)
    time.sleep(random.uniform(0.02, 0.03))
