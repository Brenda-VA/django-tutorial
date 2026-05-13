import datetime
from django.db import models
from django.utils import timezone

""" estas clases de python se convertiran e tablas sql:
y cada vez que cambie o actualice models.py debo ejecutar: 
        - python manage.py makemigrations -> Para avisarle a Django que he creado nuevos modelos
        - python manage.py migrate -> Para que cree las nuevas tablas en la bbdd
        
y el flujo seria: Modelo Python -> Migración -> Tabla en base de datos         """
class Question(models.Model):
    # columna tipo texto
    question_text = models.CharField(max_length=200)

    # columna tipo fecha
    pub_date = models.DateTimeField("date published")

    # cómo se mostrará este objeto en Django admin, shell, etc
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # relación MANY TO ONE: muchas Choice pertenecen a una Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #texto de la opcion
    choice_text = models.CharField(max_length=200)
    #votos iniciales
    votes = models.IntegerField(default=0)

    """ representsacion visual del objeto: 
    def __str__(self) ->                ANTES:                          AHORA:
                            <Question: Question object (1)>      <Question: What's new?>               """
    def __str__(self):
            return self.choice_text
    
    def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


