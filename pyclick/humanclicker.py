import time
import pyautogui as pag
from pyclick.humancurve import HumanCurve

def setup_pag():
    # Any duration less than this is rounded to 0.0 to instantly move the mouse.
    pag.MINIMUM_DURATION = 0  # Default: 0.1
    # Minimal number of seconds to sleep between mouse moves.
    pag.MINIMUM_SLEEP = 0  # Default: 0.05
    # The number of seconds to pause after EVERY public function call.
    pag.PAUSE = 0.000  # Default: 0.1

setup_pag()

class HumanClicker():
    def __init__(self):
        pass

    def move(self, toPoint, duration=2, humanCurve=None):
        fromPoint = pag.position()
        if not humanCurve:
            humanCurve = HumanCurve(fromPoint, toPoint)

        #pag.PAUSE = .001
        pag.PAUSE = duration / len(humanCurve.points)
        for point in humanCurve.points:
            pag.moveTo(point)
            
        pag.PAUSE = 0
        
    def quick_move(self, point, d):
    
        pag.MINIMUM_DURATION = 0.1
        pag.MINIMUM_SLEEP = 0.05
        pag.PAUSE = 0.1
        pag.moveTo(point[0],point[1],d)


    def click(self):
        pag.click()
        
    def right_click(self):
        pag.rightClick()
        
    def shift_click(self):
        pag.keyDown('shift')
        time.sleep(.25)
        pag.click()
        time.sleep(.25)
        pag.keyUp('shift')





