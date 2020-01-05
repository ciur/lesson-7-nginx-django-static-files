from .base import *

DEBUG = True

STATIC_URL = '/prefix/'

ALLOWED_HOSTS = [
    'mysite.test'
]

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.app'
