class Color():
    def __init__(self, color):
        self._color = color
        
    @property
    def colorValue(self):
        return self._color

    @colorValue.setter
    def colorValue(self, value):
        self._color = value