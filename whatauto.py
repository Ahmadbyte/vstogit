import pyautogui
import time
time.sleep(9)
count =0
while count<=30:
    pyautogui.typewrite("hacked "+str(count))
    pyautogui.press("enter")
    count=count+1
