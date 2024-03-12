from django.apps import AppConfig


class ListingsConfig(AppConfig):
    name = 'listings'

    def ready(self):
        pass
        # from .scheduler import scheduler
        # scheduler.start()
