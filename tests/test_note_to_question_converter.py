import unittest
from entity.note.bullet_point_note import BulletPointNote
from handler.note_to_question_converter import NoteToQuestionConverter


class TestNoteToQuestionConverter(unittest.TestCase):
    def test_bullet_point_note_with_multiple_choice_question(self):
        converter = NoteToQuestionConverter()
        note_example = BulletPointNote("Biochemical cascade of events",
                                       ["Closing of channels to the outer segment",
                                        "This causes hyperpolarization in the cell body",
                                        "Reduction of neurotransmitter glutamate at the synaptic level"])
        question, answer = converter.convert(note_example, "multiple_choice")
        print()
