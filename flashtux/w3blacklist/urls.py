#
# Copyright (C) 1999-2023 Sébastien Helleu <flashcode@flashtux.org>
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

"""URLs for W3BlackList menu."""

# pylint: disable=invalid-name, no-value-for-parameter

from django.urls import path, re_path
from django.views.generic.base import TemplateView

from flashtux.w3blacklist.views import sites, letters

urlpatterns = [
    path('sites/', sites, {'status': 'blacklist'}, name='w3blacklist_sites'),
    re_path(r'^sites/(?P<status>(blacklist|fixed))/$', sites,
            name='w3blacklist_sites_status'),
    path('sites/<int:site_id>/', sites, name='w3blacklist_site'),
    path('doc/', TemplateView.as_view(template_name='w3blacklist/doc.html'),
         name='w3blacklist_doc'),
    path('letters/', letters, name='w3blacklist_letters'),
    path('faq/', TemplateView.as_view(template_name='w3blacklist/faq.html'),
         name='w3blacklist_faq'),
]
