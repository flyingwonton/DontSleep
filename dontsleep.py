import pyautogui
import sys, time
#pyautogui.FAILSAFE = False #the failsafe will otherwise be triggered if the mouse is manually moved to a corner
screenWidth, screenHeight = pyautogui.size()

def cursormovement(timespan, delay):
    try:
        time.sleep(int(delay) * 60)
        pyautogui.moveTo(screenWidth, 0)
        pyautogui.moveTo(0, int(screenHeight) - 1, duration=int(timespan) * 60)
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