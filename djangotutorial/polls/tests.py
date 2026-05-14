import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.urls import reverse

""" Probamos todas las pruebas de nuevo con 'python manage.py test polls' en cmd, nos devuelve:
Ran 3 tests in 0.001s
OK
Destroying test database for alias 'default'... """
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """  was_published_recently() returns False for questions whose pub_date is in the future 
        comprueba que una pregunta con fecha futura No se connsidere como reciente  """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

#añadimos 2 pruebas más a la misma clase para que las pruebas seann mas completas
    def test_was_published_recently_with_old_question(self):
        """ Comprueba que una pregunta de más de 1 día NO se considera reciente. """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """ Comprueba que una pregunta publicada dentro de las últimas 24 horas sí es reciente. """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

def create_question(question_text, days):
    """ Crea una pregunta con una fecha relativa a hoy:  - days negativo = pregunta publicada en el pasado.
                                                         - days positivo = pregunta programada para el futuro. """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self): #revisa el mensaje «No polls are available.» y verifica que latest_question_list este vacia
        """ Si no hay preguntas, se muestra un mensaje adecuado """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self): #crea una pregunta y verifica que esté en la lista
        """ Las preguntas publicadas en el pasado aparecen en el index. """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))

        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self): #crea una pregunta con pub_date en el futuro, la bbdd se reinicia para cada emtodo de prueba por lo que la 1era preg ya no está ahi
        """ Las preguntas futuras no aparecen en el index. """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))

        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """ Si hay preguntas pasadas y futuras, solo aparecen las pasadas. """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))

        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_past_questions(self):
        """ El index puede mostrar varias preguntas pasadas ordenadas de más reciente a más antigua. """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))

        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )
