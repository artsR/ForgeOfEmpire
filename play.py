import time
import pyautogui, requests
from login import *
from manage import *


pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

driver = log_in()

pyautogui.press('esc');pyautogui.press('esc')
try:
    close = pyautogui.locateOnScreen('close_adv.png')
    pyautogui.click(pyautogui.center(close))
except:
    pass
# Zoom out the view of city:
set_screen()
time.sleep(10)
# Harvest crops - part1:
harvest_crops('position1', 'ratusz')

time.sleep(5)
# Spent points in Great Building:
spent_points(greatBuilding='rakieta')

time.sleep(3)
# Scroll the screen to the part2:
im = pyautogui.screenshot()
free_space = pyautogui.locateOnScreen('C:\\Users\\arts\\Documents\\BOT\\free_space.png',
                                    confidence=0.9)
pyautogui.moveTo(pyautogui.center(free_space)[0],pyautogui.center(free_space)[1], duration=0.25)
pyautogui.mouseDown()
pyautogui.moveTo(pyautogui.center(free_space)[0], 100, duration=0.5)
pyautogui.mouseUp()

# Harvest crops - part2:
harvest_crops('position2', 'atena')

# Make production - algea:
make_production('factory_alg', '3')

# Scroll the screen to the part3:
im = pyautogui.screenshot()
free_space = pyautogui.locateOnScreen('C:\\Users\\arts\\Documents\\BOT\\free_space.png')
pyautogui.moveTo(pyautogui.center(free_space)[0],pyautogui.center(free_space)[1], duration=0.25)
pyautogui.mouseDown()
pyautogui.moveTo(400, pyautogui.center(free_space)[1], duration=1)
pyautogui.mouseUp()

# Harvest crops - part3:
harvest_crops('position3', 'tower')

# Make production - terrace:
make_production()

# Scroll the screen to the part4:
im = pyautogui.screenshot()
free_space = pyautogui.locateOnScreen('C:\\Users\\arts\\Documents\\BOT\\free_space.png')
pyautogui.moveTo(pyautogui.center(free_space)[0],pyautogui.center(free_space)[1], duration=0.25)
pyautogui.mouseDown()
pyautogui.moveTo(1200, pyautogui.center(free_space)[1], duration=1)
pyautogui.mouseUp()
im = pyautogui.screenshot()
free_space2 = pyautogui.locateOnScreen('C:\\Users\\arts\\Documents\\BOT\\free_space2.png')
pyautogui.moveTo(pyautogui.center(free_space2)[0],pyautogui.center(free_space2)[1], duration=0.25)
pyautogui.mouseDown()
pyautogui.moveTo(800, pyautogui.center(free_space2)[1], duration=1)
pyautogui.moveTo(800, 620, duration=1)
pyautogui.mouseUp()

# Harvest crops - part4:
harvest_crops('position4', 'lantern')

# Close all info windows about blueprints collected:
while True:
    im = pyautogui.screenshot()
    try:
        close = pyautogui.locateOnScreen('close_adv.png')
        pyautogui.click(pyautogui.center(close))
        time.sleep(2)
    except:
        break
        pass
# Make production:
make_production(building='factory_nadprzewodnik', production='3')
make_production(building='factory_dejonizator', production='3')
make_production(building='farm')

# Move to Great Building:
im = pyautogui.screenshot()
free_space3 = pyautogui.locateOnScreen('C:\\Users\\arts\\Documents\\BOT\\free_space3.png', confidence=0.7)
pyautogui.moveTo(pyautogui.center(free_space3)[0],pyautogui.center(free_space3)[1], duration=0.25)
pyautogui.mouseDown()
pyautogui.moveTo(100, pyautogui.center(free_space3)[1]+100, duration=1)
pyautogui.mouseUp()

# Spent points in Great Building:
spent_points(greatBuilding='rakieta')

# Move screen to tavern:
im = pyautogui.screenshot()
free_space3 = pyautogui.locateOnScreen('C:\\Users\\arts\\Documents\\BOT\\free_space3.png')
pyautogui.moveTo(pyautogui.center(free_space3)[0],pyautogui.center(free_space3)[1], duration=0.25)
pyautogui.mouseDown()
pyautogui.moveTo(pyautogui.center(free_space3)[0]+700, 800, duration=1)
pyautogui.mouseUp()
# Free tavern:
free_tavern()

# Support neighbours and friends:
support(mode='neighbour', visit_tavern=False)
support(mode='friends', visit_tavern=True)

time.sleep(5)
# Close webbrowser:
driver.close()
