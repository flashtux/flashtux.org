#
# Copyright (C) 1999-2022 Sébastien Helleu <flashcode@flashtux.org>
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

"""URLs for EciAdsl menu."""

# pylint: disable=invalid-name, no-value-for-parameter

from django.urls import path, re_path
from django.views.generic.base import TemplateView

from flashtux.common.views import DownloadView
from flashtux.eciadsl.views import doc, modems, faq
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
