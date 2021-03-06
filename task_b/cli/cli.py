"""
Project: python_assessment_3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 10/11/2020 9:52 pm
File: cli.py
"""
import sys
import threading
import time
import task_b.server.server as server
import task_b.client.client as client

HOST = '127.0.0.1'
PORT = 5555


def get_user_input():
    """Gets user input."""

    inp = input('Your question: ')

    while not inp.strip():
        print('Invalid input, please try again\n')
        inp = input('Your question: ')

    return inp


def print_header():
    """Presents initial information about this program and captures user input.

    :return: Question asked by user
    """
    print('\nWelcome! Ask the Magic 8-Ball a question below:')
    print('Enter "q" to quit the application\n')
    q = get_user_input()
    print()
    return q


def start():
    """Entry point of this program.

    Two threads are created whenever a question is asked - one for the server and another one for the client.

    This prevents blocking the main thread of the program with sockets and simulates real client-server handshakes.
    """
    q = print_header()

    while q.strip().lower() != 'q':
        server_thread = threading.Thread(name='Server thread', target=server.listen, args=(HOST, PORT))
        server_thread.start()

        print(f'{server_thread.name} started...waiting for connections...')

        client_thread = threading.Thread(name='Client thread', target=client.request, args=(q, HOST, PORT))

        print(f'{client_thread.name} starting...sending request with question...\n')

        time.sleep(1)

        client_thread.start()
        client_thread.join()

        sys.stdout.flush()
        sys.stdin.flush()

        q = print_header()

    print('Bye!\n')
