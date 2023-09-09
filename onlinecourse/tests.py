from django.test import TestCase
from .models import Question, Choice


class QuestionTests(TestCase):

    def test_create_question(self):
        """Tests creating a question."""
        question = Question.objects.create(
            content="This is a question",
            grade=100
        )
        self.assertEqual(question.content, "This is a question")
        self.assertEqual(question.grade, 100)

    def test_get_score_with_correct_answers(self):
        """Tests getting the score of a question with correct answers."""
        question = Question.objects.create(
            content="This is a question",
            grade=100
        )
        choice1 = Choice.objects.create(
            question=question,
            content="Correct answer 1",
            is_correct=True
        )
        choice2 = Choice.objects.create(
            question=question,
            content="Wrong answer 1",
            is_correct=False
        )
        self.assertTrue(question.is_get_score([choice1.id]))
        self.assertFalse(question.is_get_score([choice2.id]))

    def test_get_score_with_incorrect_answers(self):
        """Tests getting the score of a question with incorrect answers."""
        question = Question.objects.create(
            content="This is a question",
            grade=100
        )
        choice1 = Choice.objects.create(
            question=question,
            content="Wrong answer 1",
            is_correct=False
        )
        choice2 = Choice.objects.create(
            question=question,
            content="Wrong answer 2",
            is_correct=False
        )
        self.assertFalse(question.is_get_score([choice1.id, choice2.id]))