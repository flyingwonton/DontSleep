import pyautogui
import sys, time
import random
#pyautogui.FAILSAFE = False #the failsafe will otherwise be triggered if the mouse is manually moved to a corner
screenWidth, screenHeight = pyautogui.size()

def cursormovement(timespan, delay):
    try:
        time.sleep(int(delay) * 60)
        #pyautogui.moveTo(screenWidth, 0)
        t_end = time.time() + int(timespan) * 60 #time.time is the current time
        while time.time() < t_end: #as long as the current time is smaller than the ending time
            pyautogui.moveTo(random.randint(1, 800), 0) #move the mouse cursor to the X and Y integer coordinates
            pyautogui.moveTo(0, random.randint(1, 800))
    except ValueError as e:
        print("Please provide only integers as parameter values.")
        sys.exit()

def checkarguments():
    if (len(sys.argv) == 2) and sys.argv[1].isnumeric():
        args = sys.argv
        timespan = args[1]
        delay = 0
        cursormovement(timespan, delay)
    elif (len(sys.argv) == 3) and sys.argv[1].isnumeric() and sys.argv[2].isnumeric():
        args = sys.argv
        timespan, delay = args[1:]
        cursormovement(timespan, delay)
    else:
        print("Error: re-check the arguments.")
        timespan = input("How long do you want the cursors moved (in minutes): ")
        if timespan.isalpha()  or timespan.isnumeric() == False:
            print("Invalid duration. \nExiting...")
            sys.exit()
        delay = input("Starting in (in minutes): ")
        if delay.isalpha() or delay.isnumeric() == False:
            delay = 0
            print("Default delay value = 0. Assumed immediate start.")
        cursormovement(timespan, delay)

if __name__ == "__main__":
    checkarguments()