import random
import keyboard
from core import clear

#dimY = int(input("Dimentions : ")) TODO Get monitor dimentions and use them for this
dimY = 50
dimX = int(dimY * 3)
playerCoord = [int(dimX/2),int(dimY/2)]

playerDeg = 0
playerInertia = 0


def PPosCheck(playerDeg,playerCoord,playerInertia):
    print("foo") #TODO


def screenRefresh():
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




screenRefresh()
