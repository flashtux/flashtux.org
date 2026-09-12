# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Django settings for flashtux project."""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Override these values in settings_local.py for production
DEBUG = True
SECRET_KEY = 'replace-me'
ALLOWED_HOSTS = []
ADMINS = []
MANAGERS = []

TIME_ZONE = 'Europe/Paris'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = False

gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('fr', gettext('French')),
)
LANGUAGES_LOCALES = {
    'en': 'en_US',
    'fr': 'fr_FR',
}

# Themes
THEMES = (
    'light',
    'dark',
)

# Translators: this is a date format, see: http://www.php.net/date
# Translators: (note: the result string must be short, use abbreviation
# Translators: for month if possible)
DATE_FORMAT = gettext('M j, Y')

# Translators: this is a short date format, see: http://www.php.net/date
# Translators: date with only year and month
DATE_YEAR_MONTH_FORMAT = gettext('F Y')

# Translators: this is a date/time format, see: http://www.php.net/date
# Translators: (note: the result string must be short, use abbreviation
# Translators: for month if possible)
DATETIME_FORMAT = gettext('M j, Y H:i')

MEDIA_ROOT = os.path.normpath(os.path.join(BASE_DIR, '..', 'media'))
MEDIA_URL = '/media/'

FILES_ROOT = os.path.normpath(os.path.join(BASE_DIR, '..', 'files'))
FILES_URL = '/files/'

STATIC_URL = '/static/'

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_countries',
    'flashtux.coding',
    'flashtux.common',
    'flashtux.eciadsl',
    'flashtux.home',
    'flashtux.image',
    'flashtux.news',
    'flashtux.weewm',
    'flashtux.w3blacklist',
]

ROOT_URLCONF = 'flashtux.urls'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
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
    'flashtux.middleware.ThemeMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'flashtux.context_processors.theme',
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'UserAttributeSimilarityValidator'),
    },
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'MinimumLengthValidator'),
    },
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'CommonPasswordValidator'),
    },
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'NumericPasswordValidator'),
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'flashtux.db',
    },
}

ADMIN_PAGE = 'admin'

# read settings_local.py (optional file)
try:
    from flashtux.settings_local import *
except ImportError:
    pass
