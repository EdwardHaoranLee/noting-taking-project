from entity.question.question import Question


class ShortAnswerQuestion(Question):
    head: str
    body: str

    def __init__(self, head: str):
        self.head = head
        self.body = ""

    def __str__(self):
        return self.body
