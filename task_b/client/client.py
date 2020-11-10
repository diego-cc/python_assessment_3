"""
Project: python_assessment_3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 10/11/2020 7:34 pm
File: client.py
"""
import socket

from colorama import Fore, Style


def request(question: str, host: str, port: int):
    """Creates a client socket and requests an answer from the server based on the provided question.

    :param question: Question to be sent to the server
    :param host: Server host
    :param port: Server port
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f'[CLIENT] Connected...sending this question: {question}')
        s.sendall(bytes(question, encoding='utf-8'))
        data = s.recv(1024)

    print(f'{Fore.GREEN}[CLIENT] Received answer from server: {data.decode(encoding="utf-8")}')
    print(Style.RESET_ALL)
