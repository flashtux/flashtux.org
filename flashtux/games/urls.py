# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""URLs for "games" menu."""

# pylint: disable=invalid-name, no-value-for-parameter

from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('bubblebobble/',
         TemplateView.as_view(template_name='games/bubblebobble.html'),
         name='games_bubblebobble'),
    path('nibble/',
         TemplateView.as_view(template_name='games/nibble.html'),
         name='games_nibble'),
    path('demoniactris/',
         TemplateView.as_view(template_name='games/demoniactris.html'),
         name='games_demoniactris'),
    path('helltris/',
         TemplateView.as_view(template_name='games/helltris.html'),
         name='games_helltris'),
    path('demoniacfight/',
         TemplateView.as_view(template_name='games/demoniacfight.html'),
         name='games_demoniacfight'),
    path('hellfight/',
         TemplateView.as_view(template_name='games/hellfight.html'),
         name='games_hellfight'),
    path('trap/',
         TemplateView.as_view(template_name='games/trap.html'),
         name='games_trap'),
    path('xmmh/',
         TemplateView.as_view(template_name='games/xmmh.html'),
         name='games_xmmh'),
]
