import uuid

from entity.question.question import Question
from entity.answer.answer import Answer


class DB:
    def __init__(self):
        pass

    def save_question(self, question: Question, correct_answer: Answer) -> uuid.UUID:
        pass

    def get_answer(self, id: uuid.UUID) -> Answer:
        pass