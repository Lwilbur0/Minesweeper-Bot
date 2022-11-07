import pyautogui as pag
from PIL import Image
from Tile import *
import colors
import copy

#double clicks on already solved NUMBERS, something with green check not looking at numbers
#needs to make a guess when there are no for sure moves

difficulty = "easy"

class board:
    def __init__(self):
        self._boardpos = pag.locateOnScreen('easy_board.png', confidence = 0.5)
        #changes in difficulty
        self._pixels = 45
        self._halfPix = 45/2
        self._startX = self._boardpos[0] / 2 + self._halfPix
        self._startY = self._boardpos[1] / 2 + self._halfPix

        #changes in difficulty
        self._cols = 10
        self._rows = 8
        self._tiles = [[(self._startX + (x * 45) + 9,self._startY + (i * 45) + 11) for x in range(self._cols)] for i in range(self._rows)]
        self._colors = None
        # if (difficulty == "easy"):
        #     self._pixels = 45
        #     self._halfPix = 45/2
        #     self._cols = 10
        #     self._rows = 8
        # if (difficulty == "medium"):
        #     self._pixels = 45
        #     self._halfPix = 45/2
        #     self._cols = 10
        #     self._rows = 8
        # if (difficulty == "hard"):
        #     self._pixels = 45
        #     self._halfPix = 45/2
        #     self._cols = 10
        #     self._rows = 8

    def screenshot(self):
        pag.screenshot("board.png", region=(self._boardpos))

    def move(self, x, y):
        pag.moveTo(self._tiles[x][y], duration = 0)

        
    def rClick(self, x, y):
        self.move(x, y)
        pag.click(button = 'right')

    def lClick(self, x, y):
        self.move(x, y)
        pag.click(button = 'left')

    def getArr(self):
        return self._tiles

    def getRgbArray(self):
        self.screenshot()

        board = Image.open("board.png")
        # pix = board.load()
        boardRGB = board.convert("RGB")

        arr = copy.deepcopy(self._tiles)
        for k in range(len(arr[0])):
            for j in range(len(arr)):
                # print((self._tiles[j][k][0] - self._startX) * 2 + self._pixels - 13, (self._tiles[j][k][1] - self._startY) * 2 + self._pixels - 11)
                rgbVal = boardRGB.getpixel((((self._tiles[j][k][0] - self._startX) * 2 + self._pixels - 13)  ,((self._tiles[j][k][1] - self._startY) * 2 + self._pixels - 11)  ))
                # print(rgbVal)
                # print(k, " , ", j)
                arr[j][k] = rgbVal
        return arr
    def refreshArr(self, lastData):
        rgb = self.getRgbArray() 
        values = [[0]*self._cols for _ in range(self._rows)]
        if (lastData == None):
            lastData = [[0]*self._cols for _ in range(self._rows)]
        # if (lastData == None):
        #     return values
        # if data[i][x] is "flag", then make values[i][x] = "flag"
        # but rgb is rgb values not the names of colors
        # if data[i][x] is not "flag" make values[i][x] = colors.getTile(rgb[i][x]
        for x in range(self._cols):
            for i in range(self._rows):
                if (lastData[i][x] == "flag"):
                    values[i][x] = "flag"
                else:
                    values[i][x] = colors.getTile(rgb[i][x])
        return values



    # getRgbArray()

    # for j in range(rows):
    #     for k in range(cols):
    #         move(j, k)