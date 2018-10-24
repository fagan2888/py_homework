#! python3
import pyautogui
import time
import random

try:
    while True:
        x=random.randint(-1,1)
        y=random.randint(-1,1)
        print(x,y)
        pyautogui.moveRel(x, y, duration=0.2)
        time.sleep(10)
except KeyboardInterrupt:
    print('done')