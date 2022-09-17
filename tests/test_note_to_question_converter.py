import unittest
from entity.note.bullet_point_note import BulletPointNote
from handler.note_to_question_converter import NoteToQuestionConverter


class TestNoteToQuestionConverter(unittest.TestCase):
    def test_bullet_point_note_with_multiple_choice_question(self):
        converter = NoteToQuestionConverter()
        note_example = BulletPointNote("Which of the following correctly compares periodic propertirs of two elements and provides an accurate explanation for that difference?",
                                       ["The first ionization energy of A1 is greater than that of B because A1 has a larger nuclear charge then B does."])
        question, answer = converter.convert(note_example, "multiple_choice")
        print()
