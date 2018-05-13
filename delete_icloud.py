import pyautogui as pag
from time import sleep

sleep(5)
for i in range(0,3000):
    pag.click(2259,950)
    sleep(0.3)
    pag.click(3652,124)
    sleep(0.5)
    pag.click(3140,634)
    sleep(2)

print("DON DON")
