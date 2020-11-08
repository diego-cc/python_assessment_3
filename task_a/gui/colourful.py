"""
Project: python_assessment_3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 08/11/2020 8:53 pm
File: colourful.py
"""
from tkinter import *
import math

import task_a.utils.utils as utils


def run():
    """Executes the GUI program"""
    root = Tk()
    root.wm_title('Colourful')
    root.wm_minsize(width=800, height=600)
    root.geometry(
        f'800x600+{math.floor(root.winfo_screenwidth() / 2 - 400)}+{math.floor(root.winfo_screenheight() / 2 - 300)}')

    frames = []
    colours_name = []
    colours_rgb = []
    colours_hsl = []

    def handle_click():
        print('Clicked generate colours:')
        print(frames)
        
        # clear previous colours
        if len(frames):
            for f in frames:
                if f:
                    f.destroy()

        if len(colours_name):
            for c in colours_name:
                if c:
                    c.destroy()

        if len(colours_rgb):
            for c in colours_rgb:
                if c:
                    c.destroy()

        if len(colours_hsl):
            for c in colours_hsl:
                if c:
                    c.destroy()

        colours = utils.get_colours()

        init_relx = 0.1
        init_rely = 0.2
        max_relx = 0.9
        relx = init_relx
        rely = init_rely
        relx_increment = 0.15
        rely_increment = 0.25

        for c in colours:
            frame = Frame(root, width=50, height=50, bg=c.hex).place(relx=relx, rely=rely, anchor=N + W)
            colour_name = Label(root, text=c.name, fg='red').place(relx=relx, rely=rely + 0.1, anchor=N + W)
            colour_rgb = Label(root, text=c.rgb, fg='red').place(relx=relx, rely=rely + 0.15, anchor=N + W)
            # colour_hsl = Label(root, text=c.hsl, fg='red').place(relx=relx, rely=rely + 0.2, anchor=N + W)

            if relx >= max_relx:
                relx = init_relx
                rely += rely_increment
            else:
                relx += relx_increment

            frames.append(frame)
            colours_name.append(colour_name)
            colours_rgb.append(colour_rgb)
            # colours_hsl.append(colour_hsl)

    generate_colours_btn = Button(root, text='Generate colours', padx=20, pady=5, fg='red', bg='lightgreen',
                                  command=handle_click).place(relx=0.5, rely=0.05, anchor=N)

    root.mainloop()
