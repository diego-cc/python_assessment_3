"""
Project: python_assessment_3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 08/11/2020 7:10 pm
File: utils.py
"""
import random
import colourise
from typing import List


def all_colours():
    """Encapsulates full list of colours available in this program

    This function was created in order to avoid circular references

    :return: Full list of colours
    """
    import task_a.colours.colour as colour

    return [
        colour.Colour(name="Salmon", rgb=colour.RGB(r=255, g=112, b=67)),
        colour.Colour(name="Brown", rgb=colour.RGB(r=109, g=76, b=55)),
        colour.Colour(name="Tile", rgb=colour.RGB(r=255, g=110, b=64)),
        colour.Colour(name="Bright Green", rgb=colour.RGB(r=100, g=221, b=23)),
        colour.Colour(name="Baby Blue", rgb=colour.RGB(r=128, g=216, b=255)),
        colour.Colour(name="Dark Red", rgb=colour.RGB(r=216, g=27, b=96)),
        colour.Colour(name="Dark Blue", rgb=colour.RGB(r=2, g=136, b=209)),
        colour.Colour(name="Dark Yellow", rgb=colour.RGB(r=175, g=180, b=43)),
        colour.Colour(name="Ephemeral Green", rgb=colour.RGB(r=200, g=230, b=201)),
        colour.Colour(name="Orange", rgb=colour.RGB(r=255, g=171, b=64)),
        colour.Colour(name="Crimson", rgb=colour.RGB(r=221, g=44, b=0)),
        colour.Colour(name="Muddy Brown", rgb=colour.RGB(r=161, g=136, b=127)),
        colour.Colour(name="Navy Blue", rgb=colour.RGB(r=63, g=79, b=163)),
        colour.Colour(name="Pink (Standard)", rgb=colour.RGB(r=217, g=139, b=224)),
        colour.Colour(name="Aqua", rgb=colour.RGB(r=128, g=220, b=213)),
        colour.Colour(name="Sun Yellow", rgb=colour.RGB(r=255, g=238, b=0)),
        colour.Colour(name="Pool Day", rgb=colour.RGB(r=0, g=255, b=234)),
        colour.Colour(name="Grass", rgb=colour.RGB(r=0, g=255, b=98)),
        colour.Colour(name="Dark Slate Blue", rgb=colour.RGB(r=100, g=98, b=123)),
        colour.Colour(name="Dark Violet", rgb=colour.RGB(r=62, g=43, b=83)),
        colour.Colour(name="Red Wine", rgb=colour.RGB(r=129, g=59, b=109)),
        colour.Colour(name="Light Gray", rgb=colour.RGB(r=102, g=105, b=100)),
        colour.Colour(name="Forest", rgb=colour.RGB(r=70, g=134, b=104)),
        colour.Colour(name="Dark Gray", rgb=colour.RGB(r=71, g=71, b=71)),
        colour.Colour(name="Bright Pink", rgb=colour.RGB(r=232, g=98, b=252)),
        colour.Colour(name="Light Yellow", rgb=colour.RGB(r=240, g=236, b=159)),
        colour.Colour(name="Ephemeral Pink", rgb=colour.RGB(r=225, g=197, b=236)),
        colour.Colour(name="Deep Green", rgb=colour.RGB(r=44, g=60, b=16)),
        colour.Colour(name="Blue (Standard)", rgb=colour.RGB(r=4, g=112, b=225)),
        colour.Colour(name="Light Slate Blue", rgb=colour.RGB(r=179, g=193, b=203)),
        colour.Colour(name="Crystal Clear", rgb=colour.RGB(r=235, g=249, b=250)),
        colour.Colour(name="Bright Blue", rgb=colour.RGB(r=75, g=35, b=245))
    ]


def get_colours(num: int = 20, unique: bool = True):
    """Returns a random list of colours (20 by default)

    :param num: Number of colours to pick from the list
    :param unique: Whether only unique colours should be present in the final list
    :return: List of colours
    """
    import task_a.colours.colour as colour

    colours = all_colours()
    max_colours = len(colours)

    if num > max_colours and unique:
        raise ValueError(f'Sorry, only f{str(max_colours)} unique colours are supported at the moment')

    if not unique:
        if num > max_colours or num < 0:
            num = max_colours

        return random.sample(colours, num)

    selected: List[colour.Colour] = []

    for i in range(num):
        selected_colour = random.choice(colours)

        while selected_colour in selected:
            selected_colour = random.choice(colours)

        selected.append(selected_colour)

    return selected


def rgb2hex(rgb):
    """Converts RGB colours to HEX

    :param rgb: RGB colour
    :return: HEX colour as a string with a '#'
    """
    return '#' + '%02x%02x%02x' % (rgb.r, rgb.g, rgb.b)


def get_complement(c):
    """Gets complementary colour

    :param c: Base colour
    :return: Complementary colour
    """
    import task_a.colours.colour as colour

    complement = colourise.complement_rgb(r=c.rgb.r, g=c.rgb.g, b=c.rgb.b)
    return colour.Colour(name=f'{c.name} (Complement)',
                         rgb=colour.RGB(r=int(complement[0]), g=int(complement[1]), b=int(complement[2])))


def get_complements(colours):
    """Converts all colours in a list to their respective complements

    :param colours: Colours to be converted
    :return: List of complements
    """
    return list(map(lambda c: get_complement(c), colours))
