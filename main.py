"""
Project: python_assessment_3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 08/11/2020 9:15 pm
File: main.py
"""
import sys
import task_a.gui.colourful as colourful


def init():
    print('Welcome! Choose which program you want to run.')
    print('Simply enter a number (e.g. 1) and press Enter.')
    print('Type "q" and press Enter to quit.')
    print('\n')

    print(
        'Option 1: Task A - Colourful: A GUI application that displays random colours and their respective complements')
    print('Option 2: Task B - A Magic 8-ball CLI application')
    print('Option 3: Task C - A signal handler CLI application')
    print('\n')

    def get_input():
        choice = input('Your choice: ')
        while choice.strip() not in ('1', '2', '3', 'Q', 'q'):
            print('Invalid choice, please try again.')
            choice = input('Your choice: ')

        return choice.strip()

    selected = get_input()

    if selected == '1':
        colourful.run()
    elif selected == '2':
        print('To be implemented')
    elif selected == '3':
        print('To be implemented')
    else:
        sys.exit(0)


init()
