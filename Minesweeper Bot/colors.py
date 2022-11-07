import copy
from board import *
# from webcolors import rgb_to_name

blank = (210, 185, 157)
blank2 = (224, 195, 163)
green = (172, 206, 94)
green2 = (180, 212, 101)
num1 = (37,122,207)
#65, 126, 198
#72,135,199
num2 = (73,147,69)
num3 = (211,49,50)
num4 = (127,39,161)
num5 = (1, 144, 253)
num6 = (165, 153, 0)
#find accurate rgbs

stockNames = [blank, blank2, green, green2, num1, num2, num3, num4, num5, num6]


# def getColor(rgbArr):
#     colors = copy.deepcopy(rgbArr)
#     for j in range(len(rgbArr)):
#         for k in range(len(rgbArr[0])):
#             print(rgbArr[j][k])
#             colors[j][k] = '%02x%02x%02x' % rgbArr[j][k]
#     return colors

def getTile(input):
    stockIdx = 100

    for i in range(len(stockNames)):
        if colorNear(stockNames[i], input):
            stockIdx = i
    
    switcher = {
        0: "blank",
        1: "blank",
        2: "green",
        3: "green",
        4: "num1",
        5: "num2",
        6: "num3",
        7: "num4",
        8: "num5",
        9: "num6",
    }
    return switcher.get(stockIdx, "nothing")

def colorNear(a, b):
    for i in range(3):
        
        if abs(a[i] - b[i]) > 30: 
            test = False
        else: test = True

        if test == False: return False
    return True
#Green:
#(172, 206, 94) = #ACCE5E
#(180, 212, 101)= #B4D465
#
