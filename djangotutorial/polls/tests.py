import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question

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