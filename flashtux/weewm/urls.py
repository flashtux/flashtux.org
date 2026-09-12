# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""URLs for WeeWM menu."""

from django.urls import path, re_path
from django.views.generic.base import TemplateView

from flashtux.common.views import DownloadView
from flashtux.image.views import images
from flashtux.weewm.views import doc

urlpatterns = [
    path('screenshots/', images,
         kwargs={
             'section': 'weewm',
             'category': 'screenshot',
             'template': 'screenshots.html',
         },
         name='weewm_screenshots'),
    path('screenshots/<str:filename>/', images,
         kwargs={
             'section': 'weewm',
             'category': 'screenshot',
             'template': 'screenshots.html',
         },
         name='weewm_screenshot'),
    path('doc/', doc, name='weewm_doc'),
    re_path(r'^download(?:/(?P<version>(stable|devel|old)))?/$',
            DownloadView.as_view(template_name='weewm/download.html'),
            name='weewm_download'),
    path('support/', TemplateView.as_view(template_name='weewm/support.html'),
         name='weewm_support'),
]
