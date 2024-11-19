from django.apps import AppConfig


class ClassnestBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'classnest_Base'
    def ready(self):
        import classnest_Base.signals  # Import signals when the app is ready
    
