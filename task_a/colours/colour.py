"""
Project: python_assessment_3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 08/11/2020 7:11 pm
File: colour.py
"""
from typing import Optional


class RGB:
    def __init__(self, r: int, g: int, b: int):
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


class HSL:
    def __init__(self, h: float, s: float, l: float):
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


class Colour:
    def __init__(self, name: str, rgb: RGB, hsl: Optional[HSL] = None):
        self.__name = name
        self.__rgb = rgb
        self.__hsl = hsl

    @property
    def name(self):
        return self.__name

    @property
    def rgb(self):
        return self.__rgb

    @property
    def hsl(self):
        return self.__hsl
