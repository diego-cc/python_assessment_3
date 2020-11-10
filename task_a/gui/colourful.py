"""
Project: python_assessment_3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 08/11/2020 8:53 pm
File: colourful.py
"""
from tkinter import *
import math

import task_a.utils.utils as utils


class Colourful:
    """GUI component of Task A"""

    WINDOW_WIDTH = 1366
    WINDOW_HEIGHT = 768

    def __init__(self):
        self.__root = Tk()
        self.__colours = []
        self.__complements = []
        self.__frames = []
        self.__complement_frames = []
        self.__colours_name = []
        self.__complements_colours_name = []
        # self.__colours_rgb = []
        # self.__complements_colours_rgb = []
        # self.__colours_hsl = []
        # self.__complements_colours_hsl = []
        self.__colours_hex = []
        self.__complements_colours_hex = []

    def handle_generate_colours(self):
        """Event handler that runs when user clicks the `Generate colours` button.

        It basically generates one list with 10 random colours and another one with their respective complements
        (20 in total).

        The end result is a grid with variable number of rows and columns that fits the window containing each colour
        in a square frame, with their respective names and HEX values (uncomment the lines regarding RGB and HSL
        values to display them as well).

        Adjust the parameters below to create different kinds of grids.
        """

        self.__colours = utils.get_colours(num=10)
        self.__complements = utils.get_complements(colours=self.__colours)

        init_relx = 0.04
        init_rely = 0.15
        max_relx = 0.8
        relx = init_relx
        rely = init_rely
        relx_increment = 0.16
        rely_increment = 0.2
        text_y_increment = 0.03

        if len(self.__frames):
            for i, c in enumerate(self.__colours):
                self.__frames[i]['bg'] = c.hex
                self.__colours_name[i]['text'] = c.name
                # self.__colours_rgb[i]['text'] = c.rgb
                # self.__colours_hsl[i]['text'] = c.hsl
                self.__colours_hex[i]['text'] = c.hex.upper()

                self.__complement_frames[i]['bg'] = self.__complements[i].hex
                self.__complements_colours_name[i]['text'] = self.__complements[i].name
                # self.__complements_colours_rgb[i]['text'] = self.__complements[i].rgb
                # self.__complements_colours_hsl[i]['text'] = self.__complements[i].hsl
                self.__complements_colours_hex[i]['text'] = self.__complements[i].hex.upper()

                if relx + 2 * relx_increment >= max_relx:
                    # jump to next row
                    rely += rely_increment
                    relx = init_relx
                else:
                    relx += 2 * relx_increment
        else:
            for i, c in enumerate(self.__colours):
                frame = Frame(self.__root, width=50, height=50, bg=c.hex)
                frame.place(relx=relx, rely=rely, anchor=N + W)

                complement_frame = Frame(self.__root, width=50, height=50, bg=self.__complements[i].hex)
                complement_frame.place(relx=relx + relx_increment, rely=rely, anchor=N + W)

                colour_name = Label(self.__root, text=c.name, fg='red')
                colour_name.place(relx=relx, rely=rely + rely_increment / 3 + text_y_increment / 2, anchor=N + W)

                complement_colour_name = Label(self.__root, text=self.__complements[i].name, fg='red')
                complement_colour_name.place(relx=relx + relx_increment,
                                             rely=rely + rely_increment / 3 + text_y_increment / 2, anchor=N + W)

                colour_hex = Label(self.__root, text=c.hex.upper(), fg='red')
                colour_hex.place(relx=relx, rely=rely + rely_increment / 3 + 3 * text_y_increment / 2, anchor=N + W)

                complement_colour_hex = Label(self.__root, text=self.__complements[i].hex.upper(), fg='red')
                complement_colour_hex.place(relx=relx + relx_increment,
                                            rely=rely + rely_increment / 3 + 3 * text_y_increment / 2,
                                            anchor=N + W)

                # colour_rgb = Label(self.__root, text=c.rgb, fg='red')
                # colour_rgb.place(relx=relx, rely=rely + rely_increment / 3 + 3 * text_y_increment / 2, anchor=N + W)

                # complement_colour_rgb = Label(self.__root, text=self.__complements[i].rgb, fg='red')
                # complement_colour_rgb.place(relx=relx + relx_increment,
                #                             rely=rely + rely_increment / 3 + 3 * text_y_increment / 2,
                #                             anchor=N + W)

                # colour_hsl = Label(self.__root, text=c.hsl, fg='red')
                # colour_hsl.place(relx=relx, rely=rely + rely_increment / 3 + 5 * text_y_increment / 2, anchor=N + W)
                #
                # complement_colour_hsl = Label(self.__root, text=self.__complements[i].hsl, fg='red')
                # complement_colour_hsl.place(relx=relx + relx_increment,
                #                             rely=rely + rely_increment / 3 + 5 * text_y_increment / 2, anchor=N + W)

                self.__frames.append(frame)
                self.__colours_name.append(colour_name)
                # self.__colours_rgb.append(colour_rgb)
                # self.__colours_hsl.append(colour_hsl)
                self.__colours_hex.append(colour_hex)

                self.__complement_frames.append(complement_frame)
                self.__complements_colours_name.append(complement_colour_name)
                # self.__complements_colours_rgb.append(complement_colour_rgb)
                # self.__complements_colours_hsl.append(complement_colour_hsl)
                self.__complements_colours_hex.append(complement_colour_hex)

                if relx + 2 * relx_increment >= max_relx:
                    # jump to next row
                    rely += rely_increment
                    relx = init_relx
                else:
                    relx += 2 * relx_increment

    def run(self):
        """Executes the GUI program"""

        self.__root.wm_title('Colourful')
        self.__root.wm_minsize(width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT)
        self.__root.geometry(
            f'800x600+{math.floor(self.__root.winfo_screenwidth() / 2 - self.WINDOW_WIDTH / 2)}+{math.floor(self.__root.winfo_screenheight() / 2 - self.WINDOW_HEIGHT / 2 - 26)}')

        generate_colours_btn = Button(self.__root, text='Generate colours', padx=20, pady=5, fg='red', bg='lightgreen',
                                      command=self.handle_generate_colours)

        generate_colours_btn.place(relx=0.5, rely=0.05, anchor=N)

        self.__root.mainloop()
