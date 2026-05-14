from django.contrib import admin
from .models import Question

'''Controla el orden de los campos dentro del formulario del admin
Antes Django mostraba los campos en el orden del modelo:    - question_text
                                                            - pub_date 
Y ahora forzamos a que aparzca primero pub_date y luego question_text                                                            '''
class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]

#registramos el modelo Question en admin pero usando la configuracion personalizada QuestionAdmin
admin.site.register(Question, QuestionAdmin)#con esto podremos crear preguntas, editarlas y borrarlas
