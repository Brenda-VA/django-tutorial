from django.contrib import admin
from .models import Choice, Question

'''Controla el orden de los campos dentro del formulario del admin
Antes Django mostraba los campos en el orden del modelo:    - question_text
                                                            - pub_date 
Y ahora forzamos a que aparzca primero pub_date y luego question_text                                                            '''

class ChoiceInline(admin.StackedInline):
    model = Choice #indica que choice se editara dentro de question
    extra = 3 # Django mostrará 3 formularios vacios extra para añadir opciones

class QuestionAdmin(admin.ModelAdmin):
    '''fieldsets permite dividir el formulario del admin en bloques
    cada bloque es una tupla: ("Título del bloque", {"fields": [...]}) 
    Si el titulo es none, django no muestra encabezado para ese bloque'''
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}), # collapse hace que esta seccion pueda aparecer plegada
    ]
    # conectamos las opciones Choice con el formulario de Questions
    inlines = [ChoiceInline]

#registramos el modelo Question en admin pero usando la configuracion personalizada QuestionAdmin
admin.site.register(Question, QuestionAdmin)#con esto podremos crear preguntas, editarlas y borrarlas
admin.site.register(Choice)#ahora choice tmb se ve en el panel de admin