"""
Django settings for veterinaria project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xf)i8a6w#$-xrc(fb+2jsnw^d3&mb@y9iei+2+f((rwh#=d@)6'

# SECURITY WARNING: don't run with debug turned on in production!
#Debug True es para desarrollo del proyecto
#Debug False es pra ya poder levantarlo a produccion
DEBUG = False 

ALLOWED_HOSTS = ['*']

#Configuracion para gmail

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'loquendo.brandon@gmail.com'
EMAIL_HOST_PASSWORD = '946470607julio'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

'''
Para usar gmail hay que desbloquear captcha
https://accounts.google.com/displayunlockcaptcha
'''


# Application definition

INSTALLED_APPS = [
    #Apps django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites', #Modulo para login
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Apps de terceros
    'crispy_forms',
    'registration',
    #Mis apps
    'huellita',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'veterinaria.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates")
        ],
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

WSGI_APPLICATION = 'veterinaria.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

#BASE_DIR es la raiz del proyecto osea src
#Es decir son los archivos static dentro del proyecto
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_pro", "static"),
]

#Los archivos estaticos de staticfiles_dirs seran recepcionados por static_root
#Son los archivos estaticos fuera del proyecto y se podran usar desde otro server
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_env", "static_root")

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_env", "media_root")

#Numero de dias que tiene el usuario para activar su cuenta despues de registrarse
ACCOUNT_ACTIVATION_DAYS = 7

REGISTRATION_AUTO_LOGIN = True

#Corresponde a nuestro dominio
SITE_ID = 1

LOGIN_REDIRECT_URL = '/'

CRISPY_TEMPLATE_PACK = 'bootstrap3'
