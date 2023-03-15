import pyautogui as pag
import time
import keyboard
import os
import webbrowser
import ntplib
from datetime import datetime
file = input('Название файла:')
x = time.mktime(datetime.strptime(input('Введите время ЧЧ:ММ:СС '), "%H:%M:%S").replace(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day).timetuple())
pag.FAILSAFE = False
url = 'https://h1bymask.github.io/school/prezo.html?file=' + file + '.py'
webbrowser.open(url, new=2)
fr = open(file + "_times.txt", 'r')
times = [float(i) / 1000 for i in fr.read().split()]
real = ntplib.NTPClient().request('europe.pool.ntp.org', version=3).tx_time
time.sleep(x - real)
for t in times:
	time.sleep(t)
	pag.click(683, 384)