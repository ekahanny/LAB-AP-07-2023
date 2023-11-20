from abc import ABC

class Color(ABC):
    def describe(self):
        pass

class BaseColor(Color):
    def __init__(self, name):
        self._name = name

    def describe(self):
        return f"Warna primer {self._name}"

class ColorMixer(Color):
    def __init__(self, color1, color2):
        self._color1 = color1
        self._color2 = color2

    def describe(self):
        return f"Warna sekunder dari campuran {self._color1.describe()} dan {self._color2.describe()}"

class ColorPalette:
    def __init__(self):
        self._colors = []

    def add_color(self, color):
        self._colors.append(color)

    def describe_colors(self):
        for color in self._colors:
            print(color.describe())

red = BaseColor("Red")
blue = BaseColor("Blue")
yellow = ColorMixer(red, blue)
green = ColorMixer(yellow, blue)

palette = ColorPalette()
palette.add_color(red)
palette.add_color(blue)
palette.add_color(yellow)
palette.add_color(green)

palette.describe_colors()