from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
# Una vista en Django es una función que recibe una petición HTTP y devuelve una respuesta HTTP.
""" En este caso:
 - (request) representa la petición que llega desde el navegador.
 - HttpResponse() devuelve texto plano al navegador.
 Flujo:
navegador -> URL -> urls.py -> views.index() -> HttpResponse """

'''AHORA USAMOS VISTAS GENERICAS 'IndexView', 'DetailView' Y 'ResultsView' 
Antes escribiamos manualmente lo de buscar datos, crear el context y renderizar el template


template_name = Le dice a Django que use unn nombre de plantilla especifico en vez del nombre de plantilla generado de forma automática
Esto hace q la vista de resultados y detalle tengan un aspecto diferente cuando sean creadas, a pesar de que ambas tengan una vista generica DetailView en 2do plano   '''

class IndexView(generic.ListView):# muestra una lista de objetos
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

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
class DetailView(generic.DetailView):#muestra un objeto concreto
    model = Question
    template_name = "polls/detail.html"

"""  Vista de resultados de una pregunta concreta
 Ejemplo: /polls/34/results/ """
class ResultsView(generic.DetailView):#muestra un objeto concreto pero usando otro template
    model = Question
    template_name = "polls/results.html"


"""  Vista para votar en una pregunta concreta
 Ejemplo: /polls/34/vote/ """
def vote(request, question_id):
    # Busca la pregunta por id.
    # Si no existe, devuelve 404.
    question = get_object_or_404(Question, pk=question_id)

    try:
        # request.POST contiene los datos enviados por el formulario.
        # En detail.html todos los radios tienen: name="choice"
        # Por eso aquí podemos leer: request.POST["choice"]
        # Ese valor será el id de la opción seleccionada.
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Si no se seleccionó ninguna opción, request.POST["choice"] no existe, lo que provoca KeyError.
        # Si el id enviado no corresponde a una Choice válida, eso provoca Choice.DoesNotExist.
        #vEn ambos casos, volvemos a mostrar el formulario con un mensaje de error.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        # F("votes") + 1 significa: "haz la suma directamente en la base de datos".
        selected_choice.votes = F("votes") + 1 # Suma 1 voto a la opción seleccionada.
        selected_choice.save()

        # Después de procesar correctamente un POST, nos redirigimos a otra URL.
        # Esto evita que el voto se repita si el usuario refresca la página.
        return HttpResponseRedirect(
            reverse("polls:results", args=(question.id,))
        )
