from django.urls import path
from . import views

""" Este archivo contiene las rutas propias de la app polls.
 Django llegará a este archivo porque mysite/urls.py incluye: 'path("polls/", include("polls.urls"))'
 Eso significa:
 /polls/        -> entra aquí
 /polls/otra/   -> también podría entrar aquí si existiera esa ruta """


""" me dice que las rutas de este archivo pertenecen a la app polls, asi evitamos connflictos por si otra app tmb tiene una ruta llamada detail 
por ejemplo: polls:detail, blog:detail, products:detail.     """
app_name = "polls"

urlpatterns = [
    # Ruta vacía "" porque el prefijo /polls/ ya lo puso mysite/urls.py.
    # URL final: http://127.0.0.1:8000/polls/
    # Cuando alguien entra ahí, Django busca la funcion index dentro del archivo views y ejecuta: views.index(request) 
path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"), #cambiamos question_id por pk
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]