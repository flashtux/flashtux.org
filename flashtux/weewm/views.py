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

"""Views for WeeWM."""

from django.utils.translation import gettext

from flashtux.common.views import doc as view_doc


def doc(request):
    """WeeWM documentation."""
    versions = (
        ('weewm', gettext('WeeWM user''s guide'), ''),
    )
    languages = (
        ('fr', gettext('French')),
        ('en', gettext('English')),
    )
    return view_doc(request, 'weewm', versions, languages)
