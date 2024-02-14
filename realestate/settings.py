"""
Django settings for realestate project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print('BASE_DIR:', BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w6rm%l&xim0ivll-li$u6fg8)6k8-$7uar^f#33ht5sutw8e!#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['89.38.128.187', 'localhost', '127.0.0.1', 'dadi.ae']

REST_FRAMEWORK = {
     'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.TokenAuthentication', )
}

PASSWORDLESS_AUTH = {
   'PASSWORDLESS_AUTH_TYPES': ['EMAIL', ],
   'PASSWORDLESS_EMAIL_NOREPLY_ADDRESS': 'Info@dadi.ae',
}



# AUTH_USER_MODEL = 'listings.User'

# Application definition

INSTALLED_APPS = [
    'pages.apps.PagesConfig',
    'listings.apps.ListingsConfig',
    'realtors.apps.RealtorsConfig',
    'accounts.apps.AccountsConfig',
    'contacts.apps.ContactsConfig',
    'our_company.apps.OurCompanyConfig',
    'blog.apps.BlogConfig',
    'catalogs.apps.CatalogsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'modules.services',
    'imagekit',
    'tinymce',
    'django_admin_geomap',
    'rest_framework',
    'rest_framework.authtoken',
    'drfpasswordless',
    "phonenumber_field",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'realestate.urls'

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
            'builtins': [
                'listings.templatetags.i18n_urls',
            ]
        },
    },
]

WSGI_APPLICATION = 'realestate.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'real_estate' ,
#         'USER': 'pks',
#         'PASSWORD': 'abc123!',
#         'HOST':'localhost',
#
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# Languages
LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
    ('ar', 'Arabian'),
)


TIME_ZONE = 'UTC'

USE_I18N = True
USE_THOUSAND_SEPARATOR = True

USE_L10N = True

USE_TZ = True

SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
# print('SETTINGS_PATH:', SETTINGS_PATH)

PROJECT_ROOT = os.path.normpath(os.path.dirname(SETTINGS_PATH))
# print('PROJECT_ROOT:', PROJECT_ROOT)


LOCALE_PATHS = (
    # 'locale',
    os.path.join(PROJECT_ROOT, 'locale'),
)

# print('locale path:', os.path.join(PROJECT_ROOT, 'locale'))


TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'realestate/static'),
    os.path.join(BASE_DIR, 'dadi-main/app')
]

# Media Folder Settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

MEDIA_ROOT_1 = os.path.join(BASE_DIR, 'dadi-main/app/img')
MEDIA_URL_1 = '/img/'

# Messages
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'info@dadi.ae'
EMAIL_HOST_PASSWORD = 'wxtt uysl qcjy xixc'
