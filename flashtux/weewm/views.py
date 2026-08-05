# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Views for WeeWM."""

from django.utils.translation import gettext

from flashtux.common.views import doc as view_doc


def doc(request):
    """WeeWM documentation."""
    versions = (
        ('weewm', gettext("WeeWM user's guide"), ''),
    )
    languages = (
        ('fr', gettext('French')),
        ('en', gettext('English')),
    )
    return view_doc(request, 'weewm', versions, languages)
