import random
import string
from typing import Tuple, List

import cohere

from entity.answer.answer import Answer
from entity.note import Note
from entity.question import Question, MultipleChoiceQuestion, ShortAnswerQuestion

preset = open("/Users/edward/Desktop/developingFolder/HTN/noting-taking-project/handler/preset.txt", "r").read()


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

        wrong = NoteToQuestionConverter._generate_wrong_answer(note, options)

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

    @staticmethod
    def _generate_wrong_answer(note: Note, options: List[str]) -> str:
        corrects = ""
        for option in options:
            corrects += ("- " + option + "\n")
        prompt = preset + "These are notes about" + note.head + ":\n" + corrects + "\nFake answer: \n"

        co = cohere.Client('453sG65YkVGHreprFjQ16XyjxQCxQhRXOifbBd4N')
        text = co.generate(prompt=prompt, temperature=0).generations[0].text

        if text.find("---") != -1:
            text = text[:text.find("---")]

        text = text.strip()

        return text
