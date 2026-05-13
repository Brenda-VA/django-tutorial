from django.contrib import admin
from .models import Question
#con esto registramos el modelo Question en admin para que django sepa que debe mostrarlo en el index de admin
admin.site.register(Question)#con esto podremos crear preguntas, editarlas y borrarlas
