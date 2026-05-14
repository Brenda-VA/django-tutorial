from django.apps import AppConfig


class PollsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField" #define que tipo de ID automatico usar
    name = "django_polls" #nombre real del modulo python
    label = "polls" #nombre corto interno