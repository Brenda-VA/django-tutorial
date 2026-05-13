from django.urls import path
from . import views

""" Este archivo contiene las rutas propias de la app polls.
 Django llegará a este archivo porque mysite/urls.py incluye: 'path("polls/", include("polls.urls"))'
 Eso significa:
 /polls/        -> entra aquí
 /polls/otra/   -> también podría entrar aquí si existiera esa ruta """
urlpatterns = [
    # Ruta vacía "" porque el prefijo /polls/ ya lo puso mysite/urls.py.
    # URL final: http://127.0.0.1:8000/polls/
    # Cuando alguien entra ahí, Django busca la funcion index dentro del archivo views y ejecuta: views.index(request) 
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]