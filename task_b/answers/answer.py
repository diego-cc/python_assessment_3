"""
Project: python_assessment_3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 10/11/2020 7:01 pm
File: answer.py
"""

from enum import Enum


class AnswerOutlook(Enum):
    """Describes the outlook of an answer"""

    AFFIRMATIVE = 0,
    NON_COMMITTAL = 1,
    NEGATIVE = 2


class Answer:
    """Base class for an answer. Contains the answer text itself and an outlook to be expected."""

    def __init__(self, ans: str, outlook: AnswerOutlook):
        self.__answer = ans
        self.__outlook = outlook

    @property
    def answer(self):
        return self.__answer

    @property
    def outlook(self):
        return self.__outlook

    @staticmethod
    def get_list():
        return [
            Answer(ans='It is certain.', outlook=AnswerOutlook.AFFIRMATIVE),
            Answer(ans='It is decidedly so.', outlook=AnswerOutlook.AFFIRMATIVE),
            Answer(ans='Without a doubt.', outlook=AnswerOutlook.AFFIRMATIVE),
            Answer(ans='Yes – definitely.', outlook=AnswerOutlook.AFFIRMATIVE),
            Answer(ans='You may rely on it.', outlook=AnswerOutlook.AFFIRMATIVE),
            Answer(ans='As I see it, yes.', outlook=AnswerOutlook.AFFIRMATIVE),
            Answer(ans='Most likely.', outlook=AnswerOutlook.AFFIRMATIVE),
            Answer(ans='Most likely.', outlook=AnswerOutlook.AFFIRMATIVE),
            Answer(ans='Outlook good.', outlook=AnswerOutlook.AFFIRMATIVE),
            Answer(ans='Yes.', outlook=AnswerOutlook.AFFIRMATIVE),
            Answer(ans='Signs point to yes.', outlook=AnswerOutlook.AFFIRMATIVE),

            Answer(ans='Reply hazy, try again.', outlook=AnswerOutlook.NON_COMMITTAL),
            Answer(ans='Ask again later.', outlook=AnswerOutlook.NON_COMMITTAL),
            Answer(ans='Better not tell you now.', outlook=AnswerOutlook.NON_COMMITTAL),
            Answer(ans='Cannot predict now.', outlook=AnswerOutlook.NON_COMMITTAL),
            Answer(ans='Concentrate and ask again.', outlook=AnswerOutlook.NON_COMMITTAL),

            Answer(ans='Don\'t count on it.', outlook=AnswerOutlook.NEGATIVE),
            Answer(ans='My reply is no.', outlook=AnswerOutlook.NEGATIVE),
            Answer(ans='My sources say no.', outlook=AnswerOutlook.NEGATIVE),
            Answer(ans='Outlook not so good.', outlook=AnswerOutlook.NEGATIVE),
            Answer(ans='Very doubtful.', outlook=AnswerOutlook.NEGATIVE),
        ]

    def __str__(self):
        return self.__answer
