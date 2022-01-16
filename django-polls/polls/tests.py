import datetime
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from . import models


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """

    time = timezone.now() + datetime.timedelta(days=days)
    return models.Question.objects.create(
        question_text=question_text,
        pub_date=time,
    )


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """was_published_recently() returns False for questions
        whose pub_date is in the future."""

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = models.Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """

        delta = datetime.timedelta(days=2)
        two_days_ago = timezone.now() - delta
        question = models.Question(pub_date=two_days_ago)
        self.assertIs(question.was_published_recently(), False)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """

        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_past_questions(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """

        question = create_question(question_text="Past questions.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """

        create_question(question_text="Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        past_question = create_question(question_text="Past question", days=-30)
        create_question(question_text="Future question", days=30)

        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"], [past_question]
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """

        question_1 = create_question(question_text="Question 1", days=-30)
        question_2 = create_question(question_text="Question 2", days=-5)

        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [question_2, question_1],
        )


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """

        future_question = create_question(question_text="Future question", days=5)
        response = self.client.get(reverse("polls:detail", args=(future_question.id,)))
        self.assertAlmostEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """

        past_question = create_question(question_text="Past question", days=-5)
        response = self.client.get(reverse("polls:detail", args=(past_question.id,)))
        self.assertContains(response, past_question.question_text)
