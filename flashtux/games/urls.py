#
# SPDX-FileCopyrightText: 1999-2025 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later
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
