from entity.question.question import Question


class ShortAnswerQuestion(Question):
    body: str

    def __init__(self, body: str):
        self.body = body

    def __str__(self):
        return self.body
