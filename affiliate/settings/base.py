"""
Django settings for affiliate project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build the path so database is in the root of the project

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--7@m&j%9eq&me%v)t(fykyqhpcr88rx+vydi#zu)@iu#1oq0w*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['whale-app-8nxyk.ondigitalocean.app', 'localhost', '127.0.0.1']



# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'allauth',
    'homepage',
    'phonenumber_field',
    'allauth.account',
    'import_export',
    'allauth.socialaccount',
    'userforms',
    'corsheaders',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

SITE_ID = 1



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',


]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'affiliate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'affiliate.wsgi.application'

ACCOUNT_FORMS = {
    'signup': 'users.forms.CustomSignupForm',
}

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators



AUTHENTICATION_BACKENDS = [

    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
]


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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
print("static_root", STATIC_ROOT)
MEDIA_URL = '/media/'
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/accounts/email/'
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False



ACCOUNT_USERNAME_REQUIRED = False    # This removes the username field
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False  # a personal preference. True by default. I don't want users to be interrupted by logging in
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # a personal preference. I don't want to add 'i don't remember my username' like they did at Nintendo, it is stupid

ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'gen:email_success'  # a page to identify that email is confirmed when not logged in
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'gen:email_success'  # same but logged in

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7  # a personal preference. 3 by default
ACCOUNT_EMAIL_REQUIRED = True  # no questions here
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # as the email will be used for login
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True  # False by default
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True  # True by default
# ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login'
ACCOUNT_USERNAME_BLACKLIST = ['yomama',]
ACCOUNT_USERNAME_MIN_LENGTH = 4  # a personal preference
ACCOUNT_SESSION_REMEMBER = True  # None by default (to ask 'Remember me?'). I want the user to be always logged in
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Wealthyplace.com  '  # a personal preference

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'zurabsx@gmail.com'
EMAIL_HOST_PASSWORD = 'rmcwppfwxbhhjaet'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # !!!! very important for django-allauth specificallyimport django_heroku
import django_heroku

django_heroku.settings(locals())