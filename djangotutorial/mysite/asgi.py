"""
Configuración de ASGI para el proyecto mysite.

Expone el callable de ASGI como una variable de nivel de módulo llamada ``application``.

Para más información sobre este archivo, vea
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_asgi_application()
