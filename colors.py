from board import *

blank = (210, 185, 157)
blank2 = (224, 195, 163)
green = (172, 206, 94)
green2 = (180, 212, 101)
num1 = (37,122,207)
# num1 = 65, 126, 198
# num1 = 72,135,199
num2 = (73,147,69)
num3 = (211,49,50)
# num3 = (219,117,101)
# num3 = (211,96,85)
num4 = (127,39,161)
num5 = (250,152,33)
# num5 = (237,161,71)
num6 = (107,171,163)
# num6 = (41,156,165)
# num7 = (66,66,66)

stockNames = [blank, blank2, green, green2, num1, num2, num3, num4, num5, num6]

def getTile(input):
    stockIdx = 100

    for i in range(len(stockNames)):
        if (i == 6):
            if (red(input[0], input[1], input[2])):
                return "num3"
        elif colorNear(stockNames[i], input):
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

def red(r, g, b):
    threshold = max(r, g, b)
    return (
        threshold > 8          
        and r == threshold     # red is biggest component
        and g < threshold*0.5  # green is much smaller
        and b < threshold*0.5  # so is b
    )
