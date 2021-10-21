"""
Django settings for umeo_net project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

from .local_settings import SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['umeo-net.com', '35.73.87.24']


# Application definition

INSTALLED_APPS = [
    'django_apscheduler',
    'umeo_site',
    'users.apps.UsersConfig',
    #'umeo_site.apps.UmeoSiteConfig',
    'cola.apps.ColaConfig',
    'polls.apps.PollsConfig',#polls�Ƃ�������̃A�v���P�[�V����
    'django.contrib.admin',#�Ǘ��T�C�g
    'django.contrib.auth',#�F�؃V�X�e��
    'django.contrib.contenttypes',#�R���e���c�^�C�v�t���[�����[�N
    'django.contrib.sessions',#�Z�b�V�����t���[�����[�N
    'django.contrib.messages',#���b�Z�[�W�t���[�����[�N
    'django.contrib.staticfiles',#�ÓI�t�@�C���̊Ǘ��t���[�����[�N
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'umeo_net.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins':[
            ],
        },
    },
]

WSGI_APPLICATION = 'umeo_net.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'umeo_database',
        'USER': 'kuwayama',
        'PASSWORD': 'kta12345',
        'HOST': 'localhost',
        'PORT': '',
        # 変えるところ2: DBエンジンをPostgreSQLにして、NAMEとUSERとPASSWORDをそれぞれ編集追記してください。
    }
}


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

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = '/usr/share/nginx/html/static'
STATIC_URL = '/static/'

LOGIN_URL = 'umeo_site:login'
LOGIN_REDIRECT_URL = 'umeo_site:home'
LOGOUT_REDIRECT_URL = 'umeo_site:index'

AUTH_USER_MODEL = 'users.User'

MEDIA_ROOT = '/usr/share/nginx/html/media'



