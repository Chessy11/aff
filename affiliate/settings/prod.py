import os
import environ

from .base import *


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
 
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


ALLOWED_HOSTS = ['https://powerful-basin-74576.herokuapp.com', 'localhost']

SECRET_KEY =  env('SECRET_KEY')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
