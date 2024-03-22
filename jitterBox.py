from core import clear
import random
import time

#dimY = int(input("Dimentions : ")) TODO Get monitor dimentions and use them for this

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

def gridPrint():
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

def posReset(X,Y):
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

def posCheck(X,Y):
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

while True:
    playerY = random.randint(0,9)
    playerX = random.randint(0,19)
    clear()
    posCheck(playerX,playerY)
    gridPrint()
    posReset(playerX,playerY)
    time.sleep(0.0416)
