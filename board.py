import pyautogui as pag
from PIL import Image
from Tile import *
import colors
import time
import copy

difficulty = "hard"

class board:
    def __init__(self):
        difficulty = ""
        with open('config.txt') as f:
            line = f.readline()
            if "hard" in line:
                difficulty = "hard"
            if "medium" in line:
                difficulty = "medium"
            if "easy" in line:
                difficulty = "easy"
            print("Bot Running On:", difficulty.capitalize())
            f.close()
        if (difficulty == "easy"):
            self._boardpos = pag.locateOnScreen('easy_board.png', confidence = 0.8)
            self._pixels = 45
            self._halfPix = 45/2
            self._cols = 10
            self._rows = 8
        if (difficulty == "medium"):
            self._boardpos = pag.locateOnScreen('medium_board.png', confidence = 0.8)
            self._pixels = 30
            self._halfPix = 30/2
            self._cols = 18
            self._rows = 14
        if (difficulty == "hard"):
            self._boardpos = pag.locateOnScreen('hardboard.png', confidence = 0.8)
            self._pixels = 25
            self._halfPix = 25/2
            self._cols = 24
            self._rows = 20
        self._startX = self._boardpos[0] / 2 + self._halfPix
        self._startY = self._boardpos[1] / 2 + self._halfPix
        self._tiles = [[(self._startX + (x * self._pixels),self._startY + (i * self._pixels)) for x in range(self._cols)] for i in range(self._rows)]
        self._colors = None

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
        if difficulty == "hard":
            time.sleep(0.1)
        self.screenshot()

        board = Image.open("board.png")
        boardRGB = board.convert("RGB")

        arr = copy.deepcopy(self._tiles)
        for k in range(len(arr[0])):
            for j in range(len(arr)):
                if (difficulty == "easy"):
                    rgbVal = boardRGB.getpixel((((self._tiles[j][k][0] - self._startX) * 2 + self._pixels - 13)  ,((self._tiles[j][k][1] - self._startY) * 2 + self._pixels - 11)  ))
                if (difficulty == "medium"): 
                    rgbVal = boardRGB.getpixel((((self._tiles[j][k][0] - self._startX) * 2 + self._pixels + 5)  ,((self._tiles[j][k][1] - self._startY) * 2 + self._pixels + 8)  ))
                if (difficulty == "hard"): 
                    rgbVal = boardRGB.getpixel((((self._tiles[j][k][0] - self._startX) * 2 + self._pixels + 5.5)  ,((self._tiles[j][k][1] - self._startY) * 2 + self._pixels + 6)  ))
                arr[j][k] = rgbVal
        return arr

    def refreshArr(self, lastData):
        rgb = self.getRgbArray() 
        values = [[0]*self._cols for _ in range(self._rows)]
        if (lastData == None):
            lastData = [[0]*self._cols for _ in range(self._rows)]
        for x in range(self._cols):
            for i in range(self._rows):
                if (lastData[i][x] == "flag"):
                    values[i][x] = "flag"
                else:
                    values[i][x] = colors.getTile(rgb[i][x])
        return values