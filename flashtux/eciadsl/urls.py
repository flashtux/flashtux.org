# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""URLs for EciAdsl menu."""

# pylint: disable=invalid-name, no-value-for-parameter

from django.urls import path, re_path
from django.views.generic.base import TemplateView

from flashtux.common.views import DownloadView
from flashtux.eciadsl.views import doc, faq, modems
from flashtux.image.views import images

urlpatterns = [
    path('screenshots/', images,
         kwargs={
             'section': 'eciadsl',
             'category': 'screenshot',
             'template': 'screenshots.html',
         },
         name='eciadsl_screenshots'),
    path('screenshots/<str:filename>/', images,
         kwargs={
             'section': 'eciadsl',
             'category': 'screenshot',
             'template': 'screenshots.html',
         },
         name='eciadsl_screenshot'),
    path('doc/', doc, name='eciadsl_doc'),
    path('tutorial/',
         TemplateView.as_view(template_name='eciadsl/tutorial.html'),
         name='eciadsl_tutorial'),
    path('modems/', modems, kwargs={'status': 'all'}, name='eciadsl_modems'),
    re_path(r'^modems/(?P<status>(all|supported|maybe|notsupported))/$',
            modems,
            name='eciadsl_modems_status'),
    path('modems/<int:modem_id>/', modems, name='eciadsl_modem'),
    path('modems/', modems, name='eciadsl_modems'),
    re_path(r'^download(?:/(?P<version>(stable|devel|old)))?/$',
            DownloadView.as_view(template_name='eciadsl/download.html'),
            name='eciadsl_download'),
    path('faq/', faq, name='eciadsl_faq'),
    path('support/',
         TemplateView.as_view(template_name='eciadsl/support.html'),
         name='eciadsl_support'),
    path('story/',
         TemplateView.as_view(template_name='eciadsl/story.html'),
         name='eciadsl_story'),
    path('team/', images,
         kwargs={
             'section': 'eciadsl',
             'category': 'team',
             'template': 'team.html',
         },
         name='eciadsl_team'),
    path('team/<str:filename>/', images,
         kwargs={
             'section': 'eciadsl',
             'category': 'team',
             'template': 'team.html',
         },
         name='eciadsl_team_photo'),
]
