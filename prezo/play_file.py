import pyautogui as pag
import time
import keyboard
import os
import webbrowser

pag.FAILSAFE = False
file = input()
url = 'https://h1bymask.github.io/school/prezo.html?file=' + file + '.py'
webbrowser.open(url, new=2)
fr = open(file + "_times.txt", 'r')
times = [float(i) / 1000 for i in fr.read().split()]
while True:
	if keyboard.is_pressed('s'):
		break
	time.sleep(0.2)
for t in times:
	time.sleep(t)
	pag.click(683, 384)
