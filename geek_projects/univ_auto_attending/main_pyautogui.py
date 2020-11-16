import pyautogui
import cv2
import time

img0 = cv2.imread(r"C:\PythonWorkspace\pyauto_click\start.png")
y0 = pyautogui.locateOnScreen(img0)
q0 = pyautogui.center(y0)

pyautogui.click(q0)

time.sleep(5)

img1 = cv2.imread(r"C:\PythonWorkspace\pyauto_click\attending.png")
y1 = pyautogui.locateOnScreen(img1)
q1 = pyautogui.center(y1)

pyautogui.click(q1)

time.sleep(6)

img2 = cv2.imread(r"C:\PythonWorkspace\pyauto_click\meeting_attending_1.png")
y2 = pyautogui.locateOnScreen(img2)
q2 = pyautogui.center(y2)

pyautogui.click(q2)

time.sleep(6)

img3 = cv2.imread(r"C:\PythonWorkspace\pyauto_click\meeting_attending_2.png")
y3 = pyautogui.locateOnScreen(img3)
q3 = pyautogui.center(y3)

pyautogui.click(q3)