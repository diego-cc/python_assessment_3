"""
Project: python_assessment_3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 08/11/2020 9:15 pm
File: main.py
"""
import sys
import task_a.gui.colourful as colourful
import task_b.cli.cli as task_b_cli
import task_c.cli.cli as task_c_cli


def init():
    """Presents all three programs available"""

    print('\nWelcome! Choose which program you want to run.')
    print('Simply enter a number (e.g. 1) and press Enter.')
    print('\nType "q" and press Enter to quit.')
    print('\n')

    print(
        'Option 1: Task A - Colourful: A GUI application that displays random colours and their respective complements')
    print('Option 2: Task B - A Magic 8-ball CLI application, implemented with sockets')
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
        c = colourful.Colourful()
        c.run()
    elif selected == '2':
        task_b_cli.start()
    elif selected == '3':
        task_c_cli.start()
    else:
        print('\nBye!')
        sys.exit(0)


init()
