import os
import dj_database_url
from django.utils.log import DEFAULT_LOGGING

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET','abcdefg12345m,nasmsdmhsd,-21+w')
HEROKU_BEARER_TOKEN = os.getenv('HEROKU_BEARER_TOKEN')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('DEBUG') == 'True')
# DEBUG = True

DEFAULT_LOGGING['handlers']['console']['filters'] = []

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ['127.0.0.1']

ADMINS = (('Webmaster', os.getenv('ADMIN_EMAIL')),)

# Application definition
SITE_ID = 1
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogs',
    'allauth.account',
    'allauth.socialaccount',
    'debug_toolbar',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'textblog.urls'
TEMPLATES = [
  {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.normpath(os.path.join(BASE_DIR, 'templates')),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]


WSGI_APPLICATION = 'textblog.wsgi.application'

# All-auth setup
ACCOUNT_EMAIL_VERIFICATION = 'none'
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# if not DEBUG:
#     ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
#     ACCOUNT_CONFIRM_EMAIL_ON_GET = True
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_USERNAME_REQUIRED = False

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd2rm1sgmpd0n0a',
        'USER': 'qntwdzqrllqhug',
        'PASSWORD': os.getenv('DB_PASS'),
        'HOST': 'ec2-18-232-143-90.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
# DATABASES = {
#     'default':{
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME':os.path.join(BASE_DIR,'db.sqlite3')
#     }
# }
# db_from_env = dj_database_url.config(conn_max_age=600)
# DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
LOGIN_REDIRECT_URL = '/dashboard'

#
# EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
# SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY', False)
# SENDGRID_SANDBOX_MODE_IN_DEBUG = False
# DEFAULT_FROM_EMAIL = "bear@somewordsfor.me"
