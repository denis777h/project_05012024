from django.apps import AppConfig


class NewswConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsw'

    def ready(self):
        pass
