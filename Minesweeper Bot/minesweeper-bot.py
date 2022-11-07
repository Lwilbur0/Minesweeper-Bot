import pyautogui as pag
from board import *
import keyboard
pag.FAILSAFE = True

def get_position(image: str):
    try:
        position = pag.locateCenterOnScreen(image, confidence = 0.8)
        print(position)
        if position == None:
            print(f'{image} not found on screen...')
            return None
        else:
            x = position[0] / 2
            y = position[1] / 2
            return x, y
    except OSError as e:
        raise Exception(e)

board = board()

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

    for i in range(len(coords)):
        if (click == "right"):
            data[coords[i][0]][coords[i][1]] = "flag"
            # board.rClick(coords[i][0], coords[i][1])
        if (click == "left"):
            board.lClick(coords[i][0], coords[i][1])  
#make an array of the x,y coordinates of green tiles
#then for loop through them
#if right click, then make data[x][y] = "flag"

def solve(data):
    for j in range(len(data)):
        for k in range(len(data[0])):
            if (data[j][k][0:3] == "num"):
                near = getNear(data, j, k)
                num = int(data[j][k][-1:])
                nearGreen = near.count("green")
                nearFlag = near.count("flag")
                if (num - nearFlag == nearGreen and nearGreen != 0):
                    clickNear(data, j, k, "right")
                    print("WIP")
                if (num - nearFlag == 0 and nearGreen != 0):
                    print("AAAAAAAAAAA")
                    clickNear(data, j, k, "left")
                    # make every nearby green tile = to "flag"
                    # data[j][k] = "flag" ///

firstClick = True
lastData = None
while True:
    data = board.refreshArr(lastData)
    lastData = data
    if keyboard.is_pressed('q'):
        break
    print(data)
    solve(data)
    if (sum(x.count("green") for x in data) == 0 and firstClick == False):
        print("Solved!")
        break
    if firstClick:
        board.lClick(5, 5)
        board.lClick(5, 5)
        firstClick = False
    # print(data)
    # board.move(0, 1)




    









# def checkGreen(x, y):
#     tile = data[x][y]
#     for j in range(x - 1, y + 2):
#         for k in range(y - 1, x + 2):
#             if (data[j][k].getColor() == '#B4D465' or '#ACCE5E'):
#                 with open('saveData', 'wb') as output:
#                     pickle.dump(data[j][k], output)                

# def nearbyIncomplete(x, y):
#     inc = []
#     for j in range(x - 1, y + 2):
#         for k in range(y - 1, x + 2):
#             if (data[j][k])
            
            


# for val in arr:
#     print(str(val))

# pag.displayMousePosition()


# if __name__ == '__main__':
#     position = get_position('easy.png')
#     pag.moveTo(position, duration = 1)
#     pag.click(button='left')
#     print(position)
#     # iml = pag.screenshot(region = )