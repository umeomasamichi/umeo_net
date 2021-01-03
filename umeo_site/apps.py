from django.apps import AppConfig


class UmeoSiteConfig(AppConfig):
    name = 'umeo_site'
    def ready(self):
        from scheduler import scheduler
        scheduler.start()
