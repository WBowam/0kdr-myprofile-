#-*- coding: UTF-8 -*- 
"""
Django settings for kdr project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5kn380j9ix%fbb%z$#4leg9!zc@ul1c&r5bg%)yl2%frua$ec@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    #'debug_toolbar',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

##添加Xadmin模块
    'xadmin',
    'crispy_forms',
    'reversion',  #  需要pip install django-reversion
##添加userena模块
    'userena',
    'guardian',
    'easy_thumbnails',

    'apps.accounts',
    'apps.ncexpress',
    'stdimage',
###Django-Debug-toolbar Begin
    
    
)

#DEBUG_TOOLBAR_PATCH_SETTINGS = False

#INTERNAL_IPS = ('127.0.0.1')

# def show_toolbar(request):
#     return True

# DEBUG_TOOLBAR_CONFIG = {
#     'INTERCEPT_REDIRECTS': False,
#     'SHOW_TOOLBAR_CALLBACK': show_toolbar,
#     'HIDE_DJANGO_SQL': False,
#     'TAG': 'div',
# }

###Django-Debug-toolbar End

MIDDLEWARE_CLASSES = (
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'kdr.urls'

WSGI_APPLICATION = 'kdr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME':'0kdr',
#         'USER' :'',      # Not used with sqlite3.,
#         'PASSWORD' : '',         # Not used with sqlite3.
#         'HOST' : '',           # Set to empty string for localhost. Not used with sqlite3.
#         'PORT' : '',            # Set to empty string for default. Not used with sqlite3.
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':'kdr.db',
        'USER' :'',      # Not used with sqlite3.,
        'PASSWORD' : '',         # Not used with sqlite3.
        'HOST' : '',           # Set to empty string for localhost. Not used with sqlite3.
        'PORT' : '',            # Set to empty string for default. Not used with sqlite3.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#STATIC_URL = '/static/'


import os
settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

###MEDIA
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public/media/')
MEDIA_URL = '/media/'


##STATIC
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public/static/')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    #os.path.join(PROJECT_ROOT, 'static/'),
    )

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'public/templates/'),
    # '/usr/local/lib/python2.7/dist-packages/django_debug_toolbar-0.8.5-py2.7.egg/debug_toolbar/templates'
)



##For userena Begin
AUTHENTICATION_BACKENDS = (
        'userena.backends.UserenaAuthenticationBackend',
        'guardian.backends.ObjectPermissionBackend',
        'django.contrib.auth.backends.ModelBackend',
    )

ANONYMOUS_USER_ID = -1


AUTH_PROFILE_MODULE = 'accounts.MyProfile'
# USERENA_DISABLE_PROFILE_LIST = True
# USERENA_SIGNIN_REDIRECT_URL = '/express/listexpress/'
# USERENA_DEFAULT_PRIVACY=open
#USERENA_SIGNIN_AFTER_SIGNUP=True
#LOGIN_REDIRECT_URL ='/'
#LOGIN_REDIRECT_URL = '/express/listexpress/'
LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'


'''
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'tulpar010@gmail.com'
EMAIL_HOST_PASSWORD = 'TEST818TEST'
##For userena End

'''
DEFAULT_FROM_EMAIL='492409676@qq.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '492409676@qq.com'
EMAIL_HOST_PASSWORD = 'tul818003817par'
##For userena End

SITE_ID=1


TEMPLATE_CONTEXT_PROCESSORS=(
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    )