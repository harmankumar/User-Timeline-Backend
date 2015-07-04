from django.http import HttpResponse
from math import sin, cos, sqrt, atan2, radians
from datetime import *
from time import *
from collections import defaultdict
import pdb
import re
import sys
from time import *  
import json
# import server.settings
import simplejson
import operator
from pymongo import *
import ConfigParser 
import networkx as nx
# from logdb_graph import logdb_graph
import MySQLdb
import logging
import urllib
import urllib2
# Django settings for server project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {    	
    	'ENGINE': 'django_mongodb_engine',
	    'NAME' : 'plabro',
	    'HOST' : 'code.plabro.com',
	    'PORT' : '27017',
    },

    'plabro': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'plabro',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'code.plabro.com',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
    },

    'mongo': {
		'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'stats',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'code.plabro.com',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
    }

}

# TODO : Add

DATABASE_ROUTERS = []

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ii2s(nmdfq_m1-0xw84s2)jwgl5h5hyh+*h)0@p3t8kdzf(w+-'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'server.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'server.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'testing',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


######################### Now to create the connections #######################

config = ConfigParser.ConfigParser()
config.read("stats1.cfg")

#MONGO CONNECTION

mongo_host = config.get('MongoDB', 'hostname')
mongo_port = int(config.get('MongoDB', 'port'))

mongo_dbname = config.get('MongoDB', 'dbname')
mongo_col = config.get('MongoDB','col')
client = MongoClient(mongo_host, mongo_port)
plabrodb = client[mongo_dbname]
shoutscoll = plabrodb[mongo_col]

#MYSQL stats CONNECTION
mysql_host_stats = config.get('MySQLStats', 'hostname')
mysql_dbname_stats = config.get('MySQLStats', 'dbname')
mysql_user_stats = config.get('MySQLStats', 'user')
mysql_pass = config.get('MySQLStats', 'passwd')
conn_stats = MySQLdb.connect(host=mysql_host_stats, db=mysql_dbname_stats, user=mysql_user_stats, passwd=mysql_pass)
cur_stats = conn_stats.cursor()
conn_stats.set_character_set('utf8')
cur_stats.execute('SET NAMES utf8;')
cur_stats.execute('SET CHARACTER SET utf8;')
cur_stats.execute('SET character_set_connection=utf8;')

#MYSQL plabro CONNECTION
mysql_host_plabro = config.get('MySQLPlabro', 'hostname')
mysql_dbname_plabro = config.get('MySQLPlabro', 'dbname')
mysql_user_plabro = config.get('MySQLPlabro', 'user')
mysql_pass = config.get('MySQLPlabro', 'passwd')
conn_plabro = MySQLdb.connect(host=mysql_host_plabro, db=mysql_dbname_plabro, user=mysql_user_plabro, passwd=mysql_pass)
cur_plabro = conn_plabro.cursor()
conn_plabro.set_character_set('utf8')
cur_plabro.execute('SET NAMES utf8;')
cur_plabro.execute('SET CHARACTER SET utf8;')
cur_plabro.execute('SET character_set_connection=utf8;')    

#MYSQL Engagement CONNECTION
mysql_host_engagement = config.get('MySQLEngagement', 'hostname')
mysql_dbname_engagement = config.get('MySQLEngagement', 'dbname')
mysql_user_engagement = config.get('MySQLEngagement', 'user')
mysql_pass = config.get('MySQLEngagement', 'passwd')
conn_engagement = MySQLdb.connect(host=mysql_host_engagement, db=mysql_dbname_engagement, user=mysql_user_engagement, passwd=mysql_pass)
cur_engagement = conn_engagement.cursor()
conn_engagement.set_character_set('utf8')
cur_engagement.execute('SET NAMES utf8;')
cur_engagement.execute('SET CHARACTER SET utf8;')
cur_engagement.execute('SET character_set_connection=utf8;') 