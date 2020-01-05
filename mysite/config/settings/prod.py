from .base import *

DEBUG = False

STATIC_URL = '/prefix/'

ALLOWED_HOSTS = [
    'mysite.test'
]

STATIC_ROOT = '/demo/www/public'

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.app'
