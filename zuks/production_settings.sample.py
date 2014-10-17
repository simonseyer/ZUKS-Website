"""
PRODUCTION SAMPLE
------------------
Do NOT change this file. Create a copy with the name 'local_settings.py'
and enter your environment specific settings there.

This sample settings file is for a PRODUCTION environment. Use the
'development_settings.sample.py' for development.

"""

"""
Local Django settings for zuks project.

These settings are environment specific and should not be submitted or
published.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/

For a guide how to configure a production system, see
https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/
"""

import os
from zuks import BASE_DIR, PROJECT_PATH
from zuks.settings import MIDDLEWARE_CLASSES

# Used to create absolute URLs (needed for e-mails)
BASE_URL = 'http://yourhost.de'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

# Has to be configured, because DEBUG is turned off
ALLOWED_HOSTS = [
    'yourhost.de',   # Allow domain
    '.yourhost.de',  # Also allow subdomains
    '.yourhost.de.', # Also allow FQDN and subdomains
]

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# The path, where static files should be copied by collectstatic
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

# Security

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'GENERATED KEY HERE'

# The webserver has to be configured to always serve the website by https
CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

# Emails
# See https://docs.djangoproject.com/en/1.6/ref/settings/#std:setting-EMAIL_BACKEND

# Performance

# Tweak this to improve performance by letting the database connection be persistent
CONN_MAX_AGE = 0

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

# Error reporting

# Add tuples like `('Name', 'email@yourhost.de')` to receive error mails,
# when there is a server error (500)
ADMINS = ()

# Add tuples in the same format as ADMINS to receive mails, when a requested
# page is not found (404)
MANAGERS = ()

MIDDLEWARE_CLASSES += ('django.middleware.common.BrokenLinkEmailsMiddleware',)