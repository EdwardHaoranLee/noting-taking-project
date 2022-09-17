import cohere, spacy

from entity.answer.answer import Answer

class CheckAnswerHandler:

    def __init__(self) -> None:
        pass

    def check_ans(self, input_answer : Answer, actual_answer : Answer) -> bool:

        nlp = spacy.load("en_core_web_lg")

        student_answer = nlp(input_answer.answer)
        database_answer = nlp(actual_answer.answer)
        
        if (student_answer.similarity(database_answer) >= 0.7):
            return True
        else:
            return False
