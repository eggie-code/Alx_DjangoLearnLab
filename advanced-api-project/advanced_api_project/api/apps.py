from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
<<<<<<< HEAD:advanced-api-project/advanced_api_project/api/apps.py
    name = 'api'
=======
    name = 'bookshelf'


class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        import bookshelf.signals
>>>>>>> e414b0a144ea75587cfd36b0bc33177dfb0b565b:advanced_features_and_security/LibraryProject/bookshelf/apps.py
