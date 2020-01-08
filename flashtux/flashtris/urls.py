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

"""URLs for "flashtris" menu."""

# pylint: disable=invalid-name, no-value-for-parameter

from django.conf.urls import url
from django.views.generic.base import TemplateView

from flashtux.image.views import images

urlpatterns = [
    url(r'^screenshots/$', images,
        {'section': 'flashtris', 'category': 'screenshot',
         'template': 'screenshots.html'},
        name='flashtris_screenshots'),
    url(r'^screenshots/(?P<filename>[a-zA-Z0-9_\-.]*)/$', images,
        {'section': 'flashtris', 'category': 'screenshot',
         'template': 'screenshots.html'},
        name='flashtris_screenshot'),
    url(r'^doc/$',
        TemplateView.as_view(template_name='flashtris/doc.html'),
        name='flashtris_doc'),
    url(r'^download/$',
        TemplateView.as_view(template_name='flashtris/download.html'),
        name='flashtris_download'),
    url(r'^dev/$',
        TemplateView.as_view(template_name='flashtris/dev.html'),
        name='flashtris_dev'),
    url(r'^faq/$',
        TemplateView.as_view(template_name='flashtris/faq.html'),
        name='flashtris_faq'),
    url(r'^support/$',
        TemplateView.as_view(template_name='flashtris/support.html'),
        name='flashtris_support'),
]
