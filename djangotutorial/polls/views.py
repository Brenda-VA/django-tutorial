from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Question
# Una vista en Django es una función que recibe una petición HTTP y devuelve una respuesta HTTP.
""" En este caso:
 - (request) representa la petición que llega desde el navegador.
 - HttpResponse() devuelve texto plano al navegador.

 Flujo:
navegador -> URL -> urls.py -> views.index() -> HttpResponse """
""" INDEX ANTIGUO
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.") """

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    ''' la funcion render es un atajo, toma el objeto request, busca la ruta, le pasa el diccionario context 
    y me devuelve un objeto httpResponse ya procesado'''
    return render(request, "polls/index.html", context)


"""  Vista de detalle de una pregunta concreta, ahora tenemos varias preguntas: 
                - /polls/
                - /polls/34/
                - /polls/34/results/
                - /polls/34/vote/
question_id viene de la URL, django va a sacar ese número de la URL y se lo va a pasar a la función
Ejemplo: /polls/34/ hace que question_id valga 34           

FLUJO DE TRABAJO:
mysite/urls.py
  ↓ detecta "polls/"
polls/urls.py
  ↓ detecta "<int:question_id>/"
views.detail(request, question_id=34)
  ↓
HttpResponse(...).     """
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)#busca una Questionn cuyo id(primary key) sea question_id
    except Question.DoesNotExist:#si no la encuentra, devuelve error 404
        raise Http404("Question does not exist")
    #si existe, la guarda e question
    return render(request, "polls/detail.html", {"question": question})



"""  Vista de resultados de una pregunta concreta
 Ejemplo: /polls/34/results/ """
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


"""  Vista para votar en una pregunta concreta
 Ejemplo: /polls/34/vote/ """
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
