import random
import threading
import keyboard
import time
from core import clear

#dimY = int(input("Dimentions : ")) TODO Get monitor dimentions and use them for this
dimY = 20
dimX = int(dimY * 3)

with open('playerPhys.csv', 'r') as file:
    pInit = file.readlines()
print(pInit)
pInit[0] = str(int(dimX/2))
print(pInit)
pInit[1] = str(int(dimY/2))
pInit[2] = str(0)
pInit[3] = str(0)
with open('playerPhys.csv', 'w') as file:
    file.writelines(pInit)

playerDeg = 0
playerInertia = 0

#0, X Coordinate
#1, Y Coordinate
#2, Player Rotation in degrees
#3, player inertia

def physCheck():
    with open('playerPhys.csv', 'r') as file:
        pDelta = file.readlines()
    while True:
        if(keyboard.is_pressed("d")):
            pDelta[3] += 2
        elif(keyboard.is_pressed("a")):
            pDelta[3] -= 2
        if(pDelta[3] < 0):
            pDelta[3] = 359
        elif(pDelta[3] >= 360):
            pDelta[3] = 0
        with open('playerPhys.csv', 'w') as file:
            file.writelines(pDelta)
        time.sleep(0.0416)

def screenRefresh():
    with open('playerPhys.csv', 'r') as file:
        pRead = file.readlines()
    exLineBase = ["|"]
    for i in range(0,dimX):
        exLineBase += " "
    exLineBase += "|"
    exLine = exLineBase
    while True:
        clear()
        print("#" + ("-"*dimX) + "#")
        for i in range(1,dimY-1):
            for n in range(1,dimX-1):
                if(i == pRead[1]-1):
                    if(292.6 <= pread[2] <= 337.5): #Display NorthWest pointer
                        exLine[pRead[0]-1] = "\\"
                        print("".join(str(x) for x in exLine))
                        exLine = exLineBase
                    if(pRead[2] >= 337.6 or pRead[2] <= 22.5): #Display North pointer
                        exLine[pRead[0]] = "|"
                        print("".join(str(x) for x in exLine))
                        exLine = exLineBase
                    if(22.6 <= pRead[2] <= 66.5): #Display NorthEast Pointer
                        exLine[pRead[0]+1] = "/"
                        print("".join(str(x) for x in exLine))
                        exLine = exLineBase
                if(i == pRead[1]): #Line that Player is located is drawn
                    exLine[pRead[0]] = "0"
                    print("".join(str(x) for x in exLine))
                    exLine = exLineBase
                    break
                else:
                    print("|" + " "*dimX + "|")
                    break
            else:
                print("|" + " "*dimX + "|")
        print("#" + ("-"*dimX) + "#")
        print(pRead[2])
        time.sleep(0.0416)




threading.Thread(target=screenRefresh).start()
threading.Thread(target=physCheck).start()

