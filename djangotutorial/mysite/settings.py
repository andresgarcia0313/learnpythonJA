"""
Configuración de Django para el proyecto mysite.

Generado por 'django-admin startproject' usando Django 5.1.3.

Para más información sobre este archivo, vea
https://docs.djangoproject.com/en/5.1/topics/settings/

Para la lista completa de configuraciones y sus valores, vea
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Construye rutas dentro del proyecto como esta: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Configuración de desarrollo rápido - no apto para producción
# Ver https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# ADVERTENCIA DE SEGURIDAD: ¡mantén la clave secreta usada en producción en
# secreto!
SECRET_KEY = 'django-insecure-(=@7mjtsj%lrp=!2788f3&bxow%v=szzh4z&^(zc(aws%@t=4b'

# ADVERTENCIA DE SEGURIDAD: ¡no ejecutes con debug activado en producción!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# WSGI (Web Server Gateway Interface) es un estándar que define cómo un
# servidor web debe comunicarse con las aplicaciones web en Python, como
# las que se desarrollan con Django.
WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internacionalización
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = True


# Archivos estáticos (CSS, JavaScript, Imágenes)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Tipo de campo de clave primaria predeterminado
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
