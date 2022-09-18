import unittest

from entity.answer import Answer
from handler.check_answer_handler import CheckAnswerHandler


class TestCheckAnswerHandler(unittest.TestCase):
    def test_similar_1(self):
        student_answer = Answer('Genetics is a game we play in Biology')
        test_answer = Answer(' Genetics is the study of genes and heredity')

        test = CheckAnswerHandler()
        self.assertEqual(False, test.check_similarity(student_answer, test_answer))

    def test_similar_2(self):
        student_answer = Answer('Amazon is best cloud user')
        test_answer = Answer("The best cloud service is Amazon")
        test = CheckAnswerHandler()
        self.assertEqual(True, test.check_similarity(student_answer, test_answer))

    def test_similar_3(self):
        student_answer = Answer('Amazon is the best, tomato is vegetable')
        test_answer = Answer('Amazon is the best, Dogs are blue, tomato is fruit')
        test = CheckAnswerHandler()
        self.assertEqual(False, test.check_similarity(student_answer, test_answer))

    def test_similar_4(self):
        student_answer = Answer(
            '[Closing of channels to the outer segment, This causes hyperpolarization in the cell body, Reduction of neurotransmitter glutamate at the synaptic level]')
        test_answer = Answer(
            '[This causes hyperpolarization in the cell body, Reduction of neurotransmitter glutamate at the synaptic level]')
        test = CheckAnswerHandler()
        self.assertEqual(False, test.check_similarity(student_answer, test_answer))
