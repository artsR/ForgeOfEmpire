import time
import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

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
            object = pyautogui.locateOnScreen('C:\\Users\\arts\\Documents\\BOT\\'+building+'.png',
                                            confidence=0.8)
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
    fileCOORD = open('C:\\Users\\arts\\Documents\\BOT\\'+coordfile+'.txt', 'r')
    coordList = fileCOORD.read().splitlines()
    fileCOORD.close()
    im = pyautogui.screenshot()
    anchor = pyautogui.locateOnScreen(anchor_name+'.png', confidence=0.9)
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
            pyautogui.locateOnScreen('C:\\Users\\arts\\Documents\\BOT\\points.png',
                                    confidence=0.9)
            break
        except:
            # if there isn't empty space it means that there are points to spent:
            building = pyautogui.locateOnScreen('C:\\Users\\arts\\Documents\\BOT\\'+greatBuilding+'.png',
                                            confidence=0.9)
            pyautogui.click(pyautogui.center(building))
            time.sleep(3)
            im = pyautogui.screenshot()
            try:
                topUp_max = pyautogui.locateOnScreen('C:\\Users\\arts\\Documents\\BOT\\top-up_max.png',
                                                confidence=0.9)
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
        enroll_friends = pyautogui.locateOnScreen('C:\\Users\\arts\\Documents\\BOT\\enroll_friends.png')
        pyautogui.click(pyautogui.center(enroll_friends))
    except:
        print('Not found.')
    try:
        friends = pyautogui.locateOnScreen('C:\\Users\\arts\\Documents\\BOT\\'+mode+'.png',
                                confidence=0.9)
        pyautogui.click(pyautogui.center(friends))
    except:
        pass
    fileCOORD = open('C:\\Users\\arts\\Documents\\BOT\\position_support.txt', 'r')
    coordList = fileCOORD.read().splitlines()
    fileCOORD.close()
    fileCOORD = open('C:\\Users\\arts\\Documents\\BOT\\position_visit_tavern.txt', 'r')
    coordList_t = fileCOORD.read().splitlines()
    fileCOORD.close()
    back = pyautogui.locateOnScreen('C:\\Users\\arts\\Documents\\BOT\\back.png')
    pyautogui.click(pyautogui.center(back))
    while True:
        pyautogui.click(300,200)
        try:
            close = pyautogui.locateOnScreen('close_adv.png')
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
        next_friends = pyautogui.locateOnScreen('C:\\Users\\arts\\Documents\\BOT\\next_friends.png')
        pyautogui.click(pyautogui.center(next_friends))
        if check == pyautogui.screenshot(region=(300,650, 300, 50)):
            break
    # roll friends' bar:
    roll_friends = pyautogui.locateOnScreen('C:\\Users\\arts\\Documents\\BOT\\roll_friends.png')
    pyautogui.click(pyautogui.center(roll_friends))

def free_tavern():
    '''
        Assumption: My tavern is already visible on the screen.
    '''
    im = pyautogui.screenshot()
    mytavern = pyautogui.locateOnScreen('C:\\Users\\arts\\Documents\\BOT\\mytavern.png',
                                        confidence=0.9)
    pyautogui.click(pyautogui.center(mytavern))
    time.sleep(5)
    im = pyautogui.screenshot()
    try:
        collect_silver_coins = pyautogui.locateOnScreen('C:\\Users\\arts\\Documents\\BOT\\collect_silver_coins.png',
                                                    confidence=0.9)
        pyautogui.click(pyautogui.center(collect_silver_coins))
    except:
        pass
    time.sleep(2)
    close = pyautogui.locateOnScreen('close_adv.png')
    pyautogui.click(pyautogui.center(close))
