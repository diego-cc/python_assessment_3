"""
Project: python_assessment_3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 08/11/2020 7:11 pm
File: colour.py
"""
import colourise

class RGB:
    """Helper class that defines RGB parameters for a Colour"""

    def __init__(self, r: int, g: int, b: int):
        """Creates a new RGB value for a Colour

            :param r: Red channel (0 - 255)
            :param g: Green channel (0 - 255)
            :param b: Blue channel (0 - 255)
        """
        if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
            raise ValueError('RGB values cannot be lower than 0 or greater than 255')

        self.__r = r
        self.__g = g
        self.__b = b

    @property
    def r(self):
        return self.__r

    @property
    def g(self):
        return self.__g

    @property
    def b(self):
        return self.__b

    def __str__(self):
        return f'RGB({self.r}, {self.g}, {self.b})'


class HSL:
    """Helper class that defines HSL parameters for a Colour"""

    def __init__(self, h: float, s: float, l: float):
        """Creates a new HSL value for a Colour

            :param h: Hue (0 - 360)
            :param s: Saturation (0 - 1)
            :param l: Lightness (0 - 1)
        """
        if h < 0.0 or h > 360.0 or s < 0.0 or s > 1.0 or l < 0.0 or l > 1.0:
            raise ValueError(
                'H value cannot be lower than 0.0 or greater than 360.0. S and L values cannot be lower than 0 or '
                'greater than 1.0')

        self.__h = h
        self.__s = s
        self.__l = l

    @property
    def h(self):
        return self.__h

    @property
    def s(self):
        return self.__s

    @property
    def l(self):
        return self.__l

    def __str__(self):
        return f'HSL({self.h, self.s, self.l}'


class Colour:
    """Base Colour class with name, RGB, HSL and HEX values"""

    def __init__(self, name: str, rgb: RGB):
        import task_a.utils.utils as utils

        self.__name = name
        self.__rgb = rgb
        hsl_values = colourise.rgb2hsl(rgb.r, rgb.g, rgb.b)
        self.__hsl = HSL(hsl_values[0], hsl_values[1], hsl_values[2])
        self.__hex = utils.rgb2hex(rgb=rgb)

    @property
    def name(self):
        return self.__name

    @property
    def rgb(self):
        return self.__rgb

    @property
    def hsl(self):
        return self.__hsl

    @property
    def hex(self):
        return self.__hex

    def __str__(self):
        return f'{self.name} - {self.rgb} - {self.hsl} - {self.hex}'
