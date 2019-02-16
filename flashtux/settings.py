# -*- coding: utf-8 -*-
#
# Copyright (C) 1999-2019 Sébastien Helleu <flashcode@flashtux.org>
#
# This file is part of FlashTux.org.
#
# FlashTux.org is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# FlashTux.org is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with FlashTux.org.  If not, see <https://www.gnu.org/licenses/>.
#

"""Django settings for flashtux project."""

import os

from django.utils.translation import ugettext_lazy

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = False

TIME_ZONE = 'Europe/Paris'
USE_TZ = True

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = False

LANGUAGES = (
    ('en', ugettext_lazy('English')),
    ('fr', ugettext_lazy('French')),
)
LANGUAGES_LOCALES = {
    'en': 'en_US',
    'fr': 'fr_FR',
}

# Translators: this is a date format, see: http://www.php.net/date (note: the result string must be short, use abbreviation for month if possible)
DATE_FORMAT = ugettext_lazy('M j, Y')
# Translators: this is a date format with only year and month, see: http://www.php.net/date
DATE_YEAR_MONTH_FORMAT = ugettext_lazy('F Y')
# Translators: this is a date/time format, see: http://www.php.net/date (note: the result string must be short, use abbreviation for month if possible)
DATETIME_FORMAT = ugettext_lazy('M j, Y H:i')

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

# read settings_local.py
try:
    from flashtux.settings_local import *
except ImportError:
    from warnings import warn
    warn('File "settings_local.py" not found, using default settings')
