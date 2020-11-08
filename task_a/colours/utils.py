"""
Project: python_assessment_3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 08/11/2020 7:10 pm
File: utils.py
"""
import random
from typing import List

from .colour import Colour, RGB

colours = [
    Colour(name="Salmon", rgb=RGB(r=255, g=112, b=67)),
    Colour(name="Brown", rgb=RGB(r=109, g=76, b=55)),
    Colour(name="Tile", rgb=RGB(r=255, g=110, b=64)),
    Colour(name="Bright Green", rgb=RGB(r=100, g=221, b=23)),
    Colour(name="Baby Blue", rgb=RGB(r=128, g=216, b=255)),
    Colour(name="Dark Pink", rgb=RGB(r=216, g=27, b=96)),
    Colour(name="Dark Blue", rgb=RGB(r=2, g=136, b=209)),
    Colour(name="Dark Yellow", rgb=RGB(r=175, g=180, b=43)),
    Colour(name="Ephemeral Green", rgb=RGB(r=200, g=230, b=201)),
    Colour(name="Orange", rgb=RGB(r=255, g=171, b=64)),
    Colour(name="Crimson", rgb=RGB(r=221, g=44, b=0)),
    Colour(name="Muddy Brown", rgb=RGB(r=161, g=136, b=127)),
    Colour(name="Navy Blue", rgb=RGB(r=63, g=79, b=163)),
    Colour(name="Pink (Standard)", rgb=RGB(r=217, g=139, b=224)),
    Colour(name="Aqua", rgb=RGB(r=128, g=220, b=213)),
    Colour(name="Sun Yellow", rgb=RGB(r=255, g=238, b=0)),
    Colour(name="Pool Day", rgb=RGB(r=0, g=255, b=234)),
    Colour(name="Grass", rgb=RGB(r=0, g=255, b=98)),
    Colour(name="Dark Slate Blue", rgb=RGB(r=100, g=98, b=123)),
    Colour(name="Dark Violet", rgb=RGB(r=62, g=43, b=83)),
    Colour(name="Red Wine", rgb=RGB(r=129, g=59, b=109)),
    Colour(name="Light Gray", rgb=RGB(r=102, g=105, b=100)),
    Colour(name="Forest", rgb=RGB(r=70, g=134, b=104)),
    Colour(name="Dark Gray", rgb=RGB(r=71, g=71, b=71)),
    Colour(name="Bright Pink", rgb=RGB(r=232, g=98, b=252)),
    Colour(name="Light Yellow", rgb=RGB(r=240, g=236, b=159)),
    Colour(name="Ephemeral Pink", rgb=RGB(r=225, g=197, b=236)),
    Colour(name="Deep Green", rgb=RGB(r=44, g=60, b=16)),
    Colour(name="Blue (Standard)", rgb=RGB(r=4, g=112, b=225)),
    Colour(name="Light Slate Blue", rgb=RGB(r=179, g=193, b=203)),
    Colour(name="Crystal Clear", rgb=RGB(r=235, g=249, b=250)),
    Colour(name="Bright Blue", rgb=RGB(r=75, g=35, b=245))
]


def get_colours(num: int = 20, unique: bool = True) -> List[Colour]:
    """Returns a random list of colours (20 by default)

    :param num: Number of colours to pick from the list
    :param unique: Whether only unique colours should be present in the final list
    :return: List of colours
    """
    max_colours = len(colours)

    if num > max_colours and unique:
        raise ValueError(f'Sorry, only f{str(max_colours)} unique colours are supported at the moment')

    if not unique:
        if num > max_colours or num < 0:
            num = max_colours

        return random.sample(colours, num)

    selected: List[Colour] = []

    for i in range(num):
        selected_colour = random.choice(colours)

        while selected_colour in selected:
            selected_colour = random.choice(colours)

        selected.append(selected_colour)

    return selected