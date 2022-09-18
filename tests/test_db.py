import unittest

from db.db import DB
from entity.answer.answer import Answer
from entity.question.multiple_choice_question import MultipleChoiceQuestion
from entity.question.short_answer_question import ShortAnswerQuestion


class TestDB(unittest.TestCase):
    def test_multiple_choice(self):
        db = DB()
        db.connect()
        id = db.save_question(MultipleChoiceQuestion("Biochemical cascade of events", {
            "A": "Closing of channels to the outer segment",
            "B": "This causes hyperpolarization in the cell body",
            "C": "Closing of channels to the inner segment",
            "D": "Reduction of neurotransmitter glutamate at the synaptic level"
        }), Answer("C"))
        result = db.get_answer(id).answer
        db._clean()
        db.close()
        assert "C" == result

    def test_definition(self):
        db = DB()
        db.connect()
        id = db.save_question(ShortAnswerQuestion("quantitative easing"),
                              Answer("A form of monetary policy in which a central bank purchases securities from the "
                                     "open market to reduce interest rates and increase the money supply."))
        result = db.get_answer(id).answer
        db._clean()
        db.close()
        assert "A form of monetary policy in which a central bank purchases securities from the " \
               "open market to reduce interest rates and increase the money supply." == result
