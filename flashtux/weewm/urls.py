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

"""URLs for WeeWM menu."""

# pylint: disable=invalid-name, no-value-for-parameter

from django.conf.urls import url
from django.views.generic.base import TemplateView

from flashtux.common.views import DownloadView
from flashtux.image.views import images
from flashtux.weewm.views import doc

urlpatterns = [
    url(r'^screenshots/$', images,
        {'section': 'weewm', 'category': 'screenshot',
         'template': 'screenshots.html'},
        name='weewm_screenshots'),
    url(r'^screenshots/(?P<filename>[a-zA-Z0-9_\-.]*)/$', images,
        {'section': 'weewm', 'category': 'screenshot',
         'template': 'screenshots.html'},
        name='weewm_screenshot'),
    url(r'^doc/$', doc, name='weewm_doc'),
    url(r'^download(?:/(?P<version>(stable|devel|old)))?/$',
        DownloadView.as_view(template_name='weewm/download.html'),
        name='weewm_download'),
    url(r'^support/$',
        TemplateView.as_view(template_name='weewm/support.html'),
        name='weewm_support'),
]
