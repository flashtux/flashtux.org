# -*- coding: utf-8 -*-
#
# Copyright (C) 1999-2020 Sébastien Helleu <flashcode@flashtux.org>
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

from django.conf.urls import url
from django.views.generic.base import TemplateView

from flashtux.common.views import DownloadView
from flashtux.eciadsl.views import doc, modems, faq
from flashtux.image.views import images

urlpatterns = [
    url(r'^screenshots/$', images,
        {'section': 'eciadsl', 'category': 'screenshot',
         'template': 'screenshots.html'},
        name='eciadsl_screenshots'),
    url(r'^screenshots/(?P<filename>[a-zA-Z0-9_\-.]*)/$', images,
        {'section': 'eciadsl', 'category': 'screenshot',
         'template': 'screenshots.html'},
        name='eciadsl_screenshot'),
    url(r'^doc/$', doc, name='eciadsl_doc'),
    url(r'^tutorial/$',
        TemplateView.as_view(template_name='eciadsl/tutorial.html'),
        name='eciadsl_tutorial'),
    url(r'^modems/$', modems, {'status': 'all'},
        name='eciadsl_modems'),
    url(r'^modems/(?P<status>(all|supported|maybe|notsupported))/$',
        modems,
        name='eciadsl_modems_status'),
    url(r'^modems/(?P<modem_id>([0-9]+))/$',
        modems,
        name='eciadsl_modem'),
    url(r'^modems/$', modems, name='eciadsl_modems'),
    url(r'^download(?:/(?P<version>(stable|devel|old)))?/$',
        DownloadView.as_view(template_name='eciadsl/download.html'),
        name='eciadsl_download'),
    url(r'^faq/$', faq, name='eciadsl_faq'),
    url(r'^support/$',
        TemplateView.as_view(template_name='eciadsl/support.html'),
        name='eciadsl_support'),
    url(r'^story/$',
        TemplateView.as_view(template_name='eciadsl/story.html'),
        name='eciadsl_story'),
    url(r'^team/$', images,
        {'section': 'eciadsl', 'category': 'team',
         'template': 'team.html'},
        name='eciadsl_team'),
    url(r'^team/(?P<filename>[a-zA-Z0-9_\-.]*)/$', images,
        {'section': 'eciadsl', 'category': 'team',
         'template': 'team.html'},
        name='eciadsl_team_photo'),
]
