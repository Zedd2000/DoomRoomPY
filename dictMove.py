from core import clear
from pynput.keyboard import Key, Listener
import random
import time
import threading

#dimY = int(input("Dimentions : ")) TODO Get monitor dimentions and use them for this

playerBaseSpd = 1
playerDeg = 0

x9 = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
x8 = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
x7 = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
x6 = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
x5 = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
x4 = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
x3 = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
x2 = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
x1 = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
x0 = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]

######################## Key Listener
def on_press(key):
    print('{0} pressed'.format(
        key))

#def on_release(key):
#    print('{0} release'.format(
#        key))
#    if key == Key.esc:
#        # Stop listener
#        return False
########################


def gridPrint(): # Play space is printed out.
    print("#" + ("-"*20) + "#")
    delta = "|"
    for i in x9:
        delta += i
    delta += "|"
    print(delta)
    delta = "|"
    for i in x8:
        delta += i
    delta += "|"
    print(delta)
    delta = "|"
    for i in x7:
        delta += i
    delta += "|"
    print(delta)
    delta = "|"
    for i in x6:
        delta += i
    delta += "|"
    print(delta)
    delta = "|"
    for i in x5:
        delta += i
    delta += "|"
    print(delta)
    delta = "|"
    for i in x4:
        delta += i
    delta += "|"
    print(delta)
    delta = "|"
    for i in x3:
        delta += i
    delta += "|"
    print(delta)
    delta = "|"
    for i in x2:
        delta += i
    delta += "|"
    print(delta)
    delta = "|"
    for i in x1:
        delta += i
    delta += "|"
    print(delta)
    delta = "|"
    for i in x0:
        delta += i
    delta += "|"
    print(delta)
    print("#" + ("-"*20) + "#")

def posReset(X,Y): #Player sprite removed to avoid streaking.
    if Y == 0:
        x0[X] = " "
    elif Y == 1:
        x1[X] = " "
    elif Y == 2:
        x2[X] = " "
    elif Y == 3:
        x3[X] = " "
    elif Y == 4:
        x4[X] = " "
    elif Y == 5:
        x5[X] = " "
    elif Y == 6:
        x6[X] = " "
    elif Y == 7:
        x7[X] = " "
    elif Y == 8:
        x8[X] = " "
    elif Y == 9:
        x9[X] = " "

def posCheck(X,Y): # Player position checked and displayed.
    if Y == 0:
        x0[X] = "0"
    elif Y == 1:
        x1[X] = "0"
    elif Y == 2:
        x2[X] = "0"
    elif Y == 3:
        x3[X] = "0"
    elif Y == 4:
        x4[X] = "0"
    elif Y == 5:
        x5[X] = "0"
    elif Y == 6:
        x6[X] = "0"
    elif Y == 7:
        x7[X] = "0"
    elif Y == 8:
        x8[X] = "0"
    elif Y == 9:
        x9[X] = "0"

def keyListen(): #Used to detect players keystrokes. Partial vesion of code from StackOverflow.
    with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()
def keyRotate(pDeg,rotInput): #Uses player input of A or D to rotate Player Character.
    print()

playerY = 5
playerX = 10


threading.Thread(target=keyListen).start() # Key listener put on seperate thread to allow for other processes to run as well.

while True:
    clear()



    posCheck(playerX,playerY)
    gridPrint()
    posReset(playerX,playerY)
    time.sleep(0.0416) # Pausing loop here for 0.0416 seconds to make the output 24 frames per second.
