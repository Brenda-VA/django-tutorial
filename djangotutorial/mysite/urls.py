from django.contrib import admin
from django.urls import include, path


"""  Este es el archivo principal de rutas del proyecto.
 Funciona como la "entrada general" de URLs.
 Cuando llega una petición, Django mira esta lista de arriba abajo
 para decidir qué hacer. FLUJO COMPLETO:
 Navegador
   ↓
Servidor Django (runserver)
   ↓
mysite/urls.py
   ↓
polls/urls.py
   ↓
views.index(request)
   ↓
HttpResponse(...)
   ↓
Respuesta HTTP
   ↓
Navegador
 """
urlpatterns = [
    # Si la URL empieza por /polls/, Django delega el resto de la URL al archivo polls/urls.py.
    # Ejemplo:
    # /polls/ -> mysite/urls.py detecta "polls/" -> include("polls.urls") -> polls/urls.py recibe el resto de la URL: ""
                                                                                    #   ↓
                                                                                    # ejecuta views.index
    path("polls/", include("polls.urls")),
    # Ruta del panel de administración de Django -> URL: http://127.0.0.1:8000/admin/
    path("admin/", admin.site.urls),
]