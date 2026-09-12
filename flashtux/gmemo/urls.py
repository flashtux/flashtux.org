# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""URLs for "gmemo" menu."""

from django.urls import path, re_path
from django.views.generic.base import TemplateView

from flashtux.common.views import DownloadView
from flashtux.image.views import images

urlpatterns = [
    path('screenshots/', images,
         kwargs={
             'section': 'gmemo',
             'category': 'screenshot',
             'template': 'screenshots.html',
         },
         name='gmemo_screenshots'),
    path('screenshots/<str:filename>/', images,
         kwargs={
             'section': 'gmemo',
             'category': 'screenshot',
             'template': 'screenshots.html',
         },
         name='gmemo_screenshot'),
    re_path(r'^download(?:/(?P<version>(stable|devel|old)))?/$',
            DownloadView.as_view(template_name='gmemo/download.html'),
            name='gmemo_download'),
    path('support/',
         TemplateView.as_view(template_name='gmemo/support.html'),
         name='gmemo_support'),
]
