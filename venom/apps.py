from django.apps import AppConfig


class VenomConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'venom'
    verbose_name = 'Клуб Веном'

    def ready(self):
        from . import signals
