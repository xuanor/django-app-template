import os
from django.apps import AppConfig
from django.apps import apps

from django.conf import settings

file_path = os.path.join(settings.BASE_DIR, 'modelos.html')
## Por cada modelo de la base de datos crear el archivo 
## **_confirm_delete, **_detail, **_form, **_list


class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'

    def ready(self):
    # Obtener los modelos
        modelos = apps.get_models()
        
        # Escribir el archivo HTML
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'modelos.html')
        with open(file_path, 'w') as f:
            f.write(",".join(modelos))


    



    
import os
from django.apps import AppConfig
from django.apps import apps

class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'

