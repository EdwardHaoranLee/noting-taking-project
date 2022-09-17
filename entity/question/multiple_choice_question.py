from entity.question.question import Question


class MultipleChoiceQuestion(Question):
    head: str
    body: dict

    def __init__(self, head: str, body: dict):
        self.head = head
        self.body = body
