# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

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
