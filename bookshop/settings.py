
import os
from decouple import config
from pathlib import Path
from dj_database_url import parse as dburl
import django_heroku
import environ


BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')
ALLOWED_HOSTS = ['djangotestapifor.herokuapp.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Book_API',
    'corsheaders',
    'rest_framework',
    'django_dropbox_storage',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'bookshop.urls'

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

WSGI_APPLICATION = 'bookshop.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASS': {
        'rest_framework.permission.IsAuthenticated',
        'rest_framework.pagination.LimitOffsetPagination',
    }

}

CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1:3000"
]
default_dburl = 'sqlite///' + os.path.join(BASE_DIR)

DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),

}
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#dropbox
DEFAULT_FILE_STORAGE = 'django_dropbox_storage.storage.DropboxStorage'
DROPBOX_OAUTH2_TOKEN = 'sl.AkRoS5J0OV2rfAY8_xPjp38FsZ4FaOtblK7NqyY6axCVVebzPsaefZ3CtlVY_k3FggVdpDfx5FAQ_eYtCuEcqw1w_A1nr-SVrjTOGncPBRsi-hno5m2QyhbLcMelzuBQTKyhj5U'
DROPBOX_ROOT_PATH = "media"
DROPBOX_APP_KEY = "vj9x570rybse6j2"
DROPBOX_APP_SECRET_KEY = "k95jdiq3z3xkxkv"

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

django_heroku.settings(locals())
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

FILE_UPLOAD_HANDLERS = (
    "testapp.dropbox_upload_handler.DropboxFileUploadHandler",
)

SITE_ID = 1

