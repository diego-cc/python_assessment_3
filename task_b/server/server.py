"""
Project: python_assessment_3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 10/11/2020 7:27 pm
File: server.py
"""
import socket
import random
import task_b.answers.answer as answer

all_answers = answer.Answer.get_list()


def get_random_answer() -> answer.Answer:
    """Chooses a random answer from the ones available in `all_answers`.

    See `Answer.get_list` for all possibilities.

    :return: Randomly picked answer
    """
    return random.choice(all_answers)


def listen(host: str, port: int):
    """Creates a server socket and starts listening on the specified `host` and `port`.

    Once a client has connected and a question has been received, this method sends back a random answer from
    `Answer.get_list`.

    :param host: Server host
    :param port: Server port
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()

        conn, addr = s.accept()

        with conn:
            print('[SERVER] Connected to', addr)

            while True:
                data = conn.recv(1024)

                if not data:
                    print('[SERVER] Closing connection...')
                    break
                else:
                    print(f'[SERVER] Received question from client: {data.decode(encoding="utf-8")}')

                conn.sendall(bytes(f'{str(get_random_answer())}', encoding='utf-8'))
