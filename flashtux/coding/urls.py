#
# Copyright (C) 1999-2021 Sébastien Helleu <flashcode@flashtux.org>
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

"""URLs for "coding" menu."""

# pylint: disable=invalid-name, no-value-for-parameter

from django.urls import path

from flashtux.coding.views import programs

urlpatterns = [
    path('programs/', programs, {'category': 'algorithms'},
         name='coding_programs'),
    path('programs/<slug:category>/', programs, name='coding_category'),
    path('programs/<slug:category>/<slug:name>/', programs,
         name='coding_program'),
]
