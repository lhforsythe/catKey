import os
import subprocess
import json

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

keyboardOn = True

def grabKeyboard():
    rawDeviceData = (subprocess.run(['hyprctl', 'devices', '-j'], stdout=subprocess.PIPE)).stdout
    jsonDeviceData = json.loads(rawDeviceData.decode('utf-8'))
    keyboard = jsonDeviceData['keyboards'][0]['name']
    return keyboard

def toggleKeyboard():
    global keyboardOn
    global keyboard

    if keyboardOn:
        print("k off")
        tray.setIcon(QIcon("icon-white.png"))
        os.system(
            f'hyprctl keyword "device[{keyboard}]:enabled" 1'
        )
    else:
        os.system(
            f'hyprctl keyword "device[{keyboard}]:enabled" 0'
        )
        print("k on")
        tray.setIcon(QIcon("icon-black.png"))
    keyboardOn = not keyboardOn
    
keyboard = grabKeyboard()
app = QApplication([])
icon = QIcon("icon-black.png")
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)
tray.activated.connect(toggleKeyboard)
app.exec()
