"""
Django settings for moge project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '--jyn^hqb_h(voubf(t7c)5gn$dj2gwl^+qg@bbs#2-hv&#7qp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['vip8j888.com','www.vip8j888.com','127.0.0.9','zl955.com','www.zl955.com','moge.pk5866.com']
MULTIPLE_UFL_CONFIG = {
    'vip8j888.com': 'moge.urls_81',
    'www.vip8j888.com': 'moge.urls_81',
    '127.0.0.9': 'moge.urls_82',
    'zl955.com': 'moge.urls_82',
    'www.zl955.com': 'moge.urls_82',
    'moge.pk5866.com': 'moge.urls_83',
}
# Application definition
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'django_filters',
    'captcha',
    'DjangoUeditor',
    'bbs.apps.BbsConfig',
    'users.apps.UsersConfig',
    'zl955.apps.Zl955Config',
    'vip8j888.apps.Vip8J888Config',
    'xadmin',
]
AUTH_USER_MODEL = "users.User"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'moge.middlewares.MultipleDomainMiddleware',
]

ROOT_URLCONF = 'moge.urls'

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
                # 'django.core.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'moge.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'  #中文支持，django1.8以后支持；1.8以前是zh-cn
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False   #默认是Ture，时间是utc时间，由于我们要用本地时间，所用手动修改为false！！！！


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
# )
# 上线屏蔽上面即可，开启下面即可
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")