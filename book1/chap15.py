# import subprocess
# subprocess.Popen('C:\\Windows\\System32\\calc.exe')
#
# import webbrowser
# webbrowser.open('https://baidu.com/')

# import subprocess
# subprocess.Popen(['start', 'hello.txt'], shell=True)
# import threading
# threading.Thread(target=spam)


#! python3
# stopwatch.py - A simple stopwatch program.
import time
import pyperclip
# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.\
Press Ctrl-C to quit.')
input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum=1
# Start tracking the lap times.
copytext=''
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        copytext+=('Lap #%s: %s (%s)\n' % (str(lapNum).ljust(2), str(totalTime).rjust(5), str(lapTime).rjust(5)))
        print('Lap #%s: %s (%s)' % (str(lapNum).ljust(2), str(totalTime).rjust(5), str(lapTime).rjust(5)), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    pyperclip.copy(copytext)
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
