import random
import string
from typing import Tuple

import cohere

from entity.answer.answer import Answer
from entity.note import Note
from entity.question import Question, MultipleChoiceQuestion, ShortAnswerQuestion


class NoteToQuestionConverter:
    def __init__(self):
        self.QUESTION_TYPES = {"multiple_choice": NoteToQuestionConverter._convert_to_multiple_choice,
                               "short_answer": NoteToQuestionConverter._convert_to_short_answer}

    def convert(self, note: Note, to: str) -> Tuple[Question, Answer]:
        if to not in self.QUESTION_TYPES:
            raise TypeError("Question type is not supported.")

        return self.QUESTION_TYPES[to](note)

    @staticmethod
    def _convert_to_multiple_choice(note: Note) -> Tuple[MultipleChoiceQuestion, Answer]:
        if type(note.body) != str and type(note.body) != list:
            raise TypeError("Note body type is not supported.")

        options = note.body if type(note.body) == list else [note.body]

        wrong = cohere.Client('453sG65YkVGHreprFjQ16XyjxQCxQhRXOifbBd4N').generate(prompt=note.head,
                                                                                   # model="medium",
                                                                                   temperature=0.75).generations[0].text

        idx = random.randint(0, len(options))
        options.insert(idx, wrong)

        mapping = {string.ascii_uppercase[idx]: option for idx, option in enumerate(options)}
        return MultipleChoiceQuestion("Which following option is wrong for this question: " + note.head, mapping), \
               Answer(string.ascii_uppercase[idx])

    @staticmethod
    def _convert_to_short_answer(note: Note) -> Tuple[ShortAnswerQuestion, Answer]:
        if type(note.body) == str:
            return ShortAnswerQuestion(note.head), Answer(note.body)
        elif type(note.body) == list:
            return ShortAnswerQuestion(note.head), \
                   Answer("\n".join([(str(i) + "." + note.body[i]) for i in range(len(note.body))]))
        else:
            raise TypeError("Note body type is not supported.")
