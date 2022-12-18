class Tile:
    def __init__(self, xy, rgb):
        self._coordinate = xy
        self._rgb = rgb
    def getCord(self):
        return self._coordinate
    def getColor(self):
        return self._rgb
    def __str__(self):
        sout = "rgb:" + str(self._rgb) + " at " + str(self._coordinate)
        return sout