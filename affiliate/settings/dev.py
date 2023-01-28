import os
import environ

from .base import *


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


ALLOWED_HOSTS = ['*']

SECRET_KEY =  env('SECRET_KEY')
