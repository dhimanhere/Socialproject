from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
if DEBUG:
    SECRET_KEY = 'django-insecure-b)07bz1n2sj&q5#9!@c(i44&=9cyhs2lz9u=gnjf@bp*u+vi@v'
else:
    SECRET_KEY = os.environ['SECRET_KEY']
# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'myapp',
    'customprofile',

    #external Dependencies
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    'storages',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

AUTH_USER_MODEL = 'customprofile.MyUser'

ROOT_URLCONF = 'socialproject.urls'

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

                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]


WSGI_APPLICATION = 'socialproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['PDATA'],
        'USER': os.environ['PUSER'],
        'PASSWORD': os.environ['PASS'],
        'HOST': os.environ['PHOST'],
        'PORT': '5432',
      }
    }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_URL = '/static/'

MEDIA_URL = 'media/'

MEDIA_ROOT =  'media/'

STATIC_ROOT = 'staticfiles/'

STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'static')
]

if DEBUG:
    API_KEY_T='abc'
    API_SECRET_T='abc'
    ACCESS_KEY='abc'
    ACCESS_SECRET = 'abc'

    GRAPH_TOKEN = 'abc'
    API_KEY_F='abc'
    API_SECRET_F='abc'
else:
    #Twitter Keys
    API_KEY_T=os.environ["API_KEY"]
    API_SECRET_T=os.environ["API_SECRET"]
    ACCESS_KEY=os.environ["ACCESS_KEY"]
    ACCESS_SECRET = os.environ["ACCESS_SECRET"]

    # Facebook Keys
    GRAPH_TOKEN = os.environ["GRAPH_TOKEN"]
    API_KEY_F=os.environ["API_KEY_F"]
    API_SECRET_F=os.environ["API_SECRET_F"]

if DEBUG:
    pass
else:
    AWS_QUERYSTRING_AUTH = False
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    CLOUDFRONT_DOMAIN = os.environ['CLOUDFRONT_DOMAIN']
    AWS_S3_CUSTOM_DOMAIN = os.environ['AWS_S3_CUSTOM_DOMAIN']
    AWS_LOCATION = 'staticfiles'
    STATIC_LOCATION = "static"
    # Add your path in the STATICFILES_STORAGE
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3ManifestStaticStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SOCIALACCOUNT_FORMS = {'disconnect': 'socialproject.forms.MyCustomSocialDisconnectForm'}

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',  # Set to 'js_sdk' to use the Facebook connect SDK
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],
        'APP': {
            'client_id': API_KEY_F,
            'secret': API_SECRET_F,
            'key': ''
        },
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'friends',
            'posts',
            'comments',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v13.0',
        'GRAPH_API_URL': 'https://graph.facebook.com/v13.0',
    },
    'twitter':{
        'APP': {
            'key': API_KEY_T,
            'secret': API_SECRET_T,
        }
    }
}
