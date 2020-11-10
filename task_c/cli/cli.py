"""
Project: python_assessment_3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 10/11/2020 10:20 pm
File: cli.py
"""
import signal


def get_user_input():
    """Keeps asking for user input until CTRL + C is pressed, in which case two things occur:

    - Either a KeyboardInterrupt or an EOFError exception is caught
    - A SIGINT is handled by `handle_sigint`
    """
    try:
        while True:
            input('Press CTRL + C ')
    except:
        print()
        pass


def handle_sigint(num, frame):
    """A basic signal handler for SIGINT.

    This signal was chosen because it's present on Linux, Windows and MacOS.

    :param num: Signal number
    :param frame: Current stack frame
    """
    print()
    if num == signal.Signals.SIGINT:
        print(f'\nReceived a SIGINT\n')


def start():
    """Entry point of this program"""

    signal.signal(signal.SIGINT, handle_sigint)

    print('\nWelcome! This program demonstrates handling signals in Python.\n')

    get_user_input()
