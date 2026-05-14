from django.contrib import admin
from .models import Question

'''Controla el orden de los campos dentro del formulario del admin
Antes Django mostraba los campos en el orden del modelo:    - question_text
                                                            - pub_date 
Y ahora forzamos a que aparzca primero pub_date y luego question_text                                                            '''
class QuestionAdmin(admin.ModelAdmin):
    '''fieldsets permite dividir el formulario del admin en bloques
    cada bloque es una tupla: ("Título del bloque", {"fields": [...]}) 
    Si el titulo es none, django no muestra encabezado para ese bloque'''
    fieldsets = [
        (None, {"fields": ["question_text"]}), # no tiene encabezado, de frente va el contenido
        ("Date information", {"fields": ["pub_date"]}), #muestra encabezado que dice Date information
    ]

#registramos el modelo Question en admin pero usando la configuracion personalizada QuestionAdmin
admin.site.register(Question, QuestionAdmin)#con esto podremos crear preguntas, editarlas y borrarlas
