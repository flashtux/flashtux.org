# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""URLs for "flashtris" menu."""

from django.urls import path
from django.views.generic.base import TemplateView

from flashtux.image.views import images

urlpatterns = [
    path('screenshots/', images,
         kwargs={
             'section': 'flashtris',
             'category': 'screenshot',
             'template': 'screenshots.html',
         },
         name='flashtris_screenshots'),
    path('screenshots/<str:filename>/', images,
         kwargs={
             'section': 'flashtris',
             'category': 'screenshot',
             'template': 'screenshots.html',
         },
         name='flashtris_screenshot'),
    path('doc/',
         TemplateView.as_view(template_name='flashtris/doc.html'),
         name='flashtris_doc'),
    path('download/',
         TemplateView.as_view(template_name='flashtris/download.html'),
         name='flashtris_download'),
    path('dev/',
         TemplateView.as_view(template_name='flashtris/dev.html'),
         name='flashtris_dev'),
    path('faq/',
         TemplateView.as_view(template_name='flashtris/faq.html'),
         name='flashtris_faq'),
    path('support/',
         TemplateView.as_view(template_name='flashtris/support.html'),
         name='flashtris_support'),
]
