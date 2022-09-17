from entity.note.note import Note
from entity.question.question import Question
from entity.question.multiple_choice_question import MultipleChoiceQuestion
from entity.question.short_answer_question import ShortAnswerQuestion
from entity.answer.answer import Answer
from typing import Tuple


class NoteToQuestionConverter:
    def __init__(self):
        self.QUESTION_TYPES = {"multiple_choice": self._convert_to_multiple_choice,
                               "short_answer": self._convert_to_short_answer}

    def convert(self, note: Note, to: str) -> Tuple[Question, Answer]:
        if to not in self.QUESTION_TYPES:
            raise TypeError("Question type is not supported.")

        return self.QUESTION_TYPES[to](note)

    def _convert_to_multiple_choice(self, note: Note) -> Tuple[MultipleChoiceQuestion, Answer]:
        pass

    def _convert_to_short_answer(self, note: Note) -> Tuple[ShortAnswerQuestion, Answer]:
        pass
