import pyautogui as pag
from board import *
import numpy as np
import time

pag.FAILSAFE = True

try:
    board = board()
except TypeError:
    print("Board Not Found")
    exit()
guessBorder = []
clickedTiles = []

def get_position(image: str):
    try:
        position = pag.locateCenterOnScreen(image, confidence = 0.8)
        if position == None:
            print(f'{image} not found on screen...')
            return None
        else:
            x = position[0] / 2
            y = position[1] / 2
            return x, y
    except OSError as e:
        raise Exception(e)

def isATile(x, y):
    tiles = board.getArr()
    if (x < 0 or y < 0 or x > len(tiles) - 1 or y > len(tiles[0]) - 1):
        return False
    return True

def getNear(arr, x, y):
    near = []
    if (isATile(x - 1, y - 1)):
        near.append(arr[x - 1][y - 1])
    else:
        near.append("DNE")
    if (isATile(x - 1, y)):
        near.append(arr[x - 1][y])
    else:
        near.append("DNE")
    if (isATile(x - 1, y + 1)):
        near.append(arr[x - 1][y + 1])
    else:
        near.append("DNE")   
    if (isATile(x, y - 1)):
        near.append(arr[x][y - 1])
    else:
        near.append("DNE") 
    if (isATile(x, y)):
        near.append(arr[x][y])
    else:
        near.append("DNE")
    if (isATile(x, y + 1)):
        near.append(arr[x][y + 1])
    else:
        near.append("DNE")  
    if (isATile(x + 1, y - 1)):
        near.append(arr[x + 1][y - 1])
    else:
        near.append("DNE") 
    if (isATile(x + 1, y)):
        near.append(arr[x + 1][y])
    else:
        near.append("DNE")
    if (isATile(x + 1, y + 1)):
        near.append(arr[x + 1][y + 1])
    else:
        near.append("DNE") 
    return near

def clickNear(data, x, y, click):
    coords = []
    if (isATile(x-1, y-1) and data[x - 1][y - 1] == "green"):
        coords.append((x-1,y-1))
    if (isATile(x-1, y) and data[x - 1][y] == "green"):
        coords.append((x-1, y))
    if (isATile(x-1, y+1) and data[x-1][y+1] == "green"):
        coords.append((x-1,y+1))
    if (isATile(x, y-1) and data[x][y-1] == "green"):
        coords.append((x,y-1))
    if (isATile(x, y) and data[x][y] == "green"):
        coords.append((x,y))
    if (isATile(x, y+1) and data[x][y+1] == "green"):
        coords.append((x,y+1))
    if (isATile(x+1, y-1) and data[x+1][y-1] == "green"):
        coords.append((x+1,y-1))
    if (isATile(x+1, y) and data[x+1][y] == "green"):
        coords.append((x+1,y))
    if (isATile(x+1, y+1) and data[x+1][y+1] == "green"):
        coords.append((x+1,y+1))

    if (click == "random" and len(coords) > 0):
        # pure random:
        idx = np.random.randint(len(coords))
        board.lClick(coords[idx][0], coords[idx][1])
        
        # array of all the the border tiles
        # for i in range(len(coords)):
        #     guessBorder.append(coords[i][0], coords[i][1])
        # guessBorder = [*set(guessBorder)]           
    else:
        for i in range(len(coords)):
            if (click == "right"):
                data[coords[i][0]][coords[i][1]] = "flag"
                board.rClick(coords[i][0], coords[i][1])
            if (click == "left"):
                if (coords[i][0], coords[i][1]) in clickedTiles:
                    continue
                clickedTiles.append((coords[i][0], coords[i][1]))
                board.lClick(coords[i][0], coords[i][1])  
def productRange(a, b):
    prd = a
    i = a
    while(i < b):
        prd*=i
        i+=1
    return prd

#probability equation
def combinations(n, r):
    if (n == r or r == 0):
        return 1
    else:
        if (r < n - r):
            r = n - r
    return productRange(r + 1, n) / productRange(1, n - r)

def solve(data):
    guessTiles = []
    clicked = False
    clickedTiles.clear()
    lastCheckedj = 0
    lastCheckedk = 0
    # nothings = 0
    for j in range(len(data)):
        for k in range(len(data[0])):
            #global array of clicked tiles that is checked for here
            # if data[j][k] in clickedTiles:
            #     continue
            if (data[j][k] == "nothing"):
                # print("NOTHING, RETURNS")
                return
                # nothings += 1
                # if nothings > 2:
                    #return
            if (data[j][k][0:3] == "num"):
                near = getNear(data, j, k)
                num = int(data[j][k][-1:])
                nearGreen = near.count("green")
                nearFlag = near.count("flag")
                if (num - nearFlag == nearGreen and nearGreen != 0):
                    clickNear(data, j, k, "right")
                    clicked = True
                elif (num - nearFlag == 0 and nearGreen != 0):
                    clickNear(data, j, k, "left")
                    clicked = True
                elif (nearGreen != 0):
                    guessTiles.append((j,k))
                    lastCheckedj = j
                    lastCheckedk = k   
    #guesses if can't solve
    if (clicked == False and data[lastCheckedj][lastCheckedk][0:3] == "num"):
        # finds bordering greens of all unsolvable tiles
        # for i in range(len(guessTiles)):
            # clickNear(data, guessTiles[i][0], guessTiles[i][1], "random")

        # pure random guess:
        clickNear(data, lastCheckedj, lastCheckedk, "random")


firstClick = True
lastData = None
# main loop:
try:
    while True:
        data = board.refreshArr(lastData)
        lastData = data
        if firstClick:
            board.lClick(5, 5)
            board.lClick(5, 5)
            firstClick = False
            time.sleep(0.2)
        else:
            # print(data)
            solve(data)
        if (sum(x.count("green") for x in data) == 0 and firstClick == False):
            print("Solved!")
            break
        if (sum(x.count("nothing") for x in data) >= (len(data) * len(data[0]))/4 ):
            print("Game Over")
            break
except pag.FailSafeException:
    print("Program Stopped")
    exit()
except TypeError:
    print("Board Not Found")
    exit()
    
# pag.displayMousePosition()