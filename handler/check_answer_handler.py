import spacy

from entity.answer.answer import Answer


class CheckAnswerHandler:

    @staticmethod
    def check_similarity(input_answer: Answer, actual_answer: Answer) -> bool:

        nlp = spacy.load("en_core_web_lg")

        answer_list = actual_answer.answer.strip('][').split(', ')
        input_list = input_answer.answer.strip('][').split(', ')

        if len(answer_list) != len(input_list):
            return False

        for a, i in zip(answer_list, input_list):
            student_answer = nlp(a)
            database_answer = nlp(i)

            if student_answer.similarity(database_answer) < 0.7:
                return False

        return True
