from entity.answer.answer import Answer
import cohere

class CheckAnswerHandler:

    co = cohere.Client('453sG65YkVGHreprFjQ16XyjxQCxQhRXOifbBd4N')

    def __init__(self) -> None:
        pass

    def check_ans(self, answer : Answer) -> bool:
        

        return False

