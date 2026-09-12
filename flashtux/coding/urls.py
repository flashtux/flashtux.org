# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""URLs for "coding" menu."""

from django.urls import path

from flashtux.coding.views import programs

urlpatterns = [
    path('programs/', programs, {'category': 'algorithms'},
         name='coding_programs'),
    path('programs/<slug:category>/', programs, name='coding_category'),
    path('programs/<slug:category>/<slug:name>/', programs,
         name='coding_program'),
]
