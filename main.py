# Made By Prashanth Umapathy
# Specialises is Laziness

# Libraries imported
import pyautogui 
import schedule 
import time 

# User Inputs

print('\n\n###############################################################################################')

print('Welcome to Zoom Schedulers, lazy people!! ^_^')
print('\n>>Enter the following details regarding the meeting to set it up...')
print(">>If you've reached here I'm assuming you've read the README.md and have the settings configured")
print(">>Please check all the configurations before proceeding as it may cause this program to crash otherwise")
print(">>Please keep this program running in the background at all times (if you want to run it everyday)")
print("Requirements : ( python version > 3.0 ) and ( 'schedule','pyautogui' packages installed )")
print('You can exit this program using ( Ctrl+c ) at any time')

print('\n###############################################################################################')

meet_id = input('Enter Meeting ID: ')
password = input('Enter Meeting password: ')
meet_time = input(('Enter everyday meeting time in 24hour format (eg: "15:30" for 3:30pm): '))
total_meet = input('How long will the meeting last for ?(Answer in minutes eg:120 for 2 hours): ')
print('###############################################################################################')

#just for confirmation
total_meet = int(total_meet)
meet_time = str(meet_time)

# Where the Magic happens function
def zoomClass():
    time.sleep(0.2)

    pyautogui.press('esc',interval=0.1)
    
    time.sleep(0.3)

    pyautogui.press('win',interval=0.5)
    pyautogui.write('zoom')
    pyautogui.press('enter',interval=0.5)

    time.sleep(10)

    x,y = pyautogui.locateCenterOnScreen('joinIMG.png')
    """
    # x,y = pyautogui.locateCenterOnScreen('joinIMG.png', confidence = 0.9)
    # Uncomment ln 49 and comment ln 47 
    # if you get an 'TypeError: cannot unpack non-iterable NoneType object' error
    """
    pyautogui.click(x,y)


    pyautogui.press('enter',interval=5)
    pyautogui.write(meet_id)
    pyautogui.press('enter',interval=5)

    pyautogui.write(password)
    pyautogui.press('enter',interval = 10)

    print("Session has started and will continue for %s minutes"%total_meet)

    print('Hold (Ctrl+c) to exit the program ')

    #Total time of zoom session
    time.sleep(total_meet) 

    # closing Zoom
    pyautogui.hotkey('alt','f4')
    time.sleep(0.5)
    pyautogui.hotkey('alt','f4')


# Every day at whatever time the user has entered.
schedule.every().day.at("%s"%meet_time).do(zoomClass)
print("Scheduling everyday at ",meet_time)

# Infinite Loop so that the scheduled task keeps running
while True: 

	# Check whether a scheduled task is pending to run or not
	schedule.run_pending() 
	time.sleep(1) 

# Main Func
# if __name__ == "__main__":
    # zoomClass()
