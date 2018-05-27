import time
import os

# os.path.

current_time = time.time()

def getScreenShotDir():
    teturn './screenshots'

def getPngfilename():
    screenshotsDir = getScreenShotDir()
    return screenshotsDir + str(current_time) + '.png'

