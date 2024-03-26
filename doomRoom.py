import random
import threading
import keyboard
import time
from core import clear

#dimY = int(input("Dimentions : ")) TODO Get monitor dimentions and use them for this
dimY = 40
dimX = int(dimY * 3)
playerCoord = [int(dimX/2),int(dimY/2)]

playerDeg = 0
playerInertia = 0


def physCheck(playerDeg,playerCoord,playerInertia):
    while True:
        if(keyboard.is_pressed("d")):
            playerDeg += 2
        elif(keyboard.is_pressed("a")):
            playerDeg -= 2
        if(playerDeg < 0):
            playerDeg = 359
        elif(playerDeg >= 360):
            playerDeg = 0
        #print(playerDeg)
        time.sleep(0.0416)

def screenRefresh():
    while True:
        clear()
        exLineBase = ["|"]
        for i in range(0,dimX):
            exLineBase += " "
        exLineBase += "|"
        exLine = exLineBase
        print("#" + ("-"*dimX) + "#")
        for i in range(1,dimY-1):
            for n in range(1,dimX-1):
                if(i == playerCoord[1]):
                    exLine[playerCoord[0]] = "0"
                    print("".join(str(x) for x in exLine))
                    exLine = exLineBase
                    break
                else:
                    print("|" + " "*dimX + "|")
                    break
            else:
                print("|" + " "*dimX + "|")
        print("#" + ("-"*dimX) + "#")
        time.sleep(0.0416)




threading.Thread(target=screenRefresh).start()
threading.Thread(target=physCheck(playerDeg,playerCoord,playerInertia)).start()

