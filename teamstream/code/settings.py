#Debug settings
DEBUG = True
TEMPLATE_DEBUG = DEBUG
TEMPLATE_STRING_IF_INVALID = '' #clear string

#Common project Settings
SITE_URL = 'http://127.0.0.1:8000'

import os
import sys

PROJECT_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')

# Insert parent and lib dirs to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(PROJECT_ROOT, 'code/apps')))
sys.path.insert(0, os.path.abspath(os.path.join(PROJECT_ROOT, 'code/libs')))
sys.path.insert(0, os.path.abspath(os.path.join(PROJECT_ROOT, 'code')))

#CommonMiddleware settings
PREPEND_WWW = False
APPEND_SLASH = True

#A tuple that lists people who get code error notifications.
#When DEBUG=False and a view raises an exception, Django will e-mail these people
#with the full exception information. Each member of the tuple should be a tuple of (Full name, e-mail address)
ADMINS = (
      # ('Your Name', 'your_email@domain.com'),

)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = 'teamstream'             # Or path to database file if using sqlite3.
DATABASE_USER = 'root'             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

LANGUAGES = (
  ('en', 'English'),
)

SITE_ID = 1

#DATE_FORMAT, DATETIME_FORMAT, TIME_FORMAT, YEAR_MONTH_FORMAT, MONTH_DAY_FORMAT - http://www.djangoproject.com/documentation/templates/#now#http://www.djangoproject.com/documentation/templates/#now
DATE_FORMAT = 'j N Y'
DATETIME_FORMAT = 'j N Y, H:i'
TIME_FORMAT = 'H:i'
YEAR_MONTH_FORMAT = 'F Y'
MONTH_DAY_FORMAT = 'j F'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = SITE_URL + '/media/'
STATIC_URL = SITE_URL + '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = SITE_URL + '/media-admin/'
ADMIN_MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media-admin")

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    #'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

#!WARNING - better to disable in production version
#    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, "code/templates",),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    
    # internals
    'apps.teamstream',
    'apps.lib',
)

TEMPLATE_CONTEXT_PROCESSORS = (
  # Standart
  'django.core.context_processors.auth',
  'django.core.context_processors.debug',
  'django.core.context_processors.i18n', 
  
  'django.core.context_processors.request',
)