import unittest
from entity.note.bullet_point_note import BulletPointNote
from entity.note.definition_note import DefinitionNote
from handler.note_to_question_converter import NoteToQuestionConverter


class TestNoteToQuestionConverter(unittest.TestCase):
    converter = NoteToQuestionConverter()

    def test_bullet_point_note_with_multiple_choice_question(self):
        note_example = BulletPointNote("Biochemical cascade of events",
                                       ["Closing of channels to the outer segment",
                                        "This causes hyperpolarization in the cell body",
                                        "Reduction of neurotransmitter glutamate at the synaptic level"])
        question, answer = self.converter.convert(note_example, "multiple_choice")
        print("Question:\n" + str(question))
        print("Answer: \n" + str(answer))

    def test_bullet_point_note_with_short_answer_question(self):
        note_example = BulletPointNote("Biochemical cascade of events",
                                       ["Closing of channels to the outer segment",
                                        "This causes hyperpolarization in the cell body",
                                        "Reduction of neurotransmitter glutamate at the synaptic level"])
        question, answer = self.converter.convert(note_example, "short_answer")
        print("Question:\n" + str(question))
        print("Answer: \n" + str(answer))

    def test_definition_note_with_short_answer_question(self):
        note_example = DefinitionNote("Pneumoconiosis",
                                      "A group of lung diseases caused by the lung's reaction inhaling certain dusts.")
        question, answer = self.converter.convert(note_example, "short_answer")
        print("Question:\n" + str(question))
        print("Answer: \n" + str(answer))

