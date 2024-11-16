"""
Configuración WSGI para el proyecto mysite.

Expone el callable WSGI como una variable de nivel de módulo llamada ``application``.

Para más información sobre este archivo, vea
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
