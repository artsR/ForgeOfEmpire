import os
import time
import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

basedir = os.path.abspath(os.path.driname(__file__))
ITEMS_TO_COLLECT = os.path.join(basedir, 'items_to_collect')
BUTTONS = os.path.join(basedir, 'buttons')
AREA_COORDS = os.path.join(basedir, 'area_coords')

# Make production:
def make_production(building='terrace', production='6'):
    ''' arguments:
        building - name of file with production building e.x. terrace.
        production - is a number of key which should be pressed to active
                production of wanted duration e.x. 8 hours.
        (name of files without extensions)
    '''
    while True:
        time.sleep(2)
        im = pyautogui.screenshot()
        try:
            object = pyautogui.locateOnScreen(
                os.path.join(ITEMS_TO_COLLECT, f'{building}.png') , confidence=0.8
            )
            pyautogui.click(pyautogui.center(object))
            time.sleep(2)
            pyautogui.press(production)
            # make sure that window will be closed even if production was in hand:
            time.sleep(2)
            pyautogui.press('esc');pyautogui.press('esc')
        except:
            break

def harvest_crops(coordfile, anchor_name):
    ''' arguments:
        coordfile - it's name of file where track of mouse is saved.
        anchor_name - building that will be clicked first to set up "harvest mode"
                    in game (to assure that first building has something to collect
                    to active "mouseDown")
        (name of files without extensions)
    '''
    fileCOORD = open(os.path.join(AREA_COORDS, f'{coordfile}.txt'), 'r')
    coordList = fileCOORD.read().splitlines()
    fileCOORD.close()
    im = pyautogui.screenshot()
    anchor = pyautogui.locateOnScreen(
        os.path.join(AREA_COORDS, f'{anchor_name}.png'), confidence=0.9
    )
    pyautogui.mouseDown(pyautogui.center(anchor))
    for move in coordList:
        coord = move.split(',')
        x = int(coord[0])
        y = int(coord[1])
        pyautogui.moveTo(x, y, duration=0.2)
    pyautogui.mouseUp()
    time.sleep(3)

def spent_points(greatBuilding='rakieta'):
    ''' arguments:
        greatBuilding - where the points should be spent:
            options:
                [rakieta, ]
    '''
    # Check if there is empty space in points bar:
    while True:
        im = pyautogui.screenshot()
        try:
            pyautogui.locateOnScreen(os.path.join(basedir, 'points.png'), confidence=0.9)
            break
        except:
            # if there isn't empty space it means that there are points to spent:
            building = pyautogui.locateOnScreen(
                os.path.join(ITEMS_TO_COLLECT, f'{greatBuilding}.png'), confidence=0.9
            )
            pyautogui.click(pyautogui.center(building))
            time.sleep(3)
            im = pyautogui.screenshot()
            try:
                topUp_max = pyautogui.locateOnScreen(
                    os.path.join(basedir, 'top-up_max.png'), confidence=0.9
                )
                pyautogui.click(pyautogui.center(topUp_max))
            except:
                pass
            pyautogui.press('esc');pyautogui.press('esc')
            #close = pyautogui.locateOnScreen('close_adv.png')
            #pyautogui.click(pyautogui.center(close))
            time.sleep(2)
            pass

def set_screen():
    # zoom out screen:
    pyautogui.click(1000,160)
    pyautogui.scroll(-100)
    pyautogui.scroll(-100)
    pyautogui.scroll(-100)
    pyautogui.scroll(-100)

def support(mode='friends', visit_tavern=True):
    ''' arguments:
        [mode]: [friends, neighbour]
        [visit_tavern]: [True, False] Do you want to visit user's tavern?
    '''
    try:
        enroll_friends = pyautogui.locateOnScreen(
            os.path.join(BUTTONS, 'enroll_friends.png')
        )
        pyautogui.click(pyautogui.center(enroll_friends))
    except:
        print('Not found.')
    try:
        friends = pyautogui.locateOnScreen(
            os.path.join(BUTTONS, f'{mode}.png'), confidence=0.9
        )
        pyautogui.click(pyautogui.center(friends))
    except:
        pass
    fileCOORD = open(os.path.join(AREA_COORDS, 'position_support.txt'), 'r')
    coordList = fileCOORD.read().splitlines()
    fileCOORD.close()
    fileCOORD = open(os.path.join(AREA_COORDS, 'position_visit_tavern.txt'), 'r')
    coordList_t = fileCOORD.read().splitlines()
    fileCOORD.close()
    back = pyautogui.locateOnScreen(os.path.join(BUTTONS, 'back.png'))
    pyautogui.click(pyautogui.center(back))
    while True:
        pyautogui.click(300,200)
        try:
            close = pyautogui.locateOnScreen(os.path.join(BUTTONS, 'close_adv.png'))
            pyautogui.click(pyautogui.center(close))
        except:
            pass
        time.sleep(0.8)
        for move, move_t in zip(coordList,coordList_t):
            coord = move.split(',')
            coord_t = move_t.split(',')
            x = int(coord[0])
            y = int(coord[1])
            x_t = int(coord_t[0])
            y_t = int(coord_t[1])
            pyautogui.click(x, y, duration=0.1)
            time.sleep(0.3)
            if visit_tavern:
                pyautogui.click(x_t, y_t, duration=0.1)
                time.sleep(2)
            pyautogui.press('esc')
            pyautogui.press('esc')
        check = pyautogui.screenshot(region=(300,650, 300, 50))
        next_friends = pyautogui.locateOnScreen(os.path.join(BUTTONS, 'next_friends.png'))
        pyautogui.click(pyautogui.center(next_friends))
        if check == pyautogui.screenshot(region=(300,650, 300, 50)):
            break
    # roll friends' bar:
    roll_friends = pyautogui.locateOnScreen(os.path.join(BUTTONS, 'roll_friends.png'))
    pyautogui.click(pyautogui.center(roll_friends))

def free_tavern():
    '''
        Assumption: My tavern is already visible on the screen.
    '''
    im = pyautogui.screenshot()
    mytavern = pyautogui.locateOnScreen(
        os.path.join(ITEMS_TO_COLLECT, 'mytavern.png'), confidence=0.9
    )
    pyautogui.click(pyautogui.center(mytavern))
    time.sleep(5)
    im = pyautogui.screenshot()
    try:
        collect_silver_coins = pyautogui.locateOnScreen(
            os.path.join(ITEMS_TO_COLLECT, 'collect_silver_coins.png'), confidence=0.9
        )
        pyautogui.click(pyautogui.center(collect_silver_coins))
    except:
        pass
    time.sleep(2)
    close = pyautogui.locateOnScreen(os.path.join(BUTTONS, 'close_adv.png'))
    pyautogui.click(pyautogui.center(close))
