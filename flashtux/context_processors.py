# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Context processors."""

from django.conf import settings
from django.utils.translation import pgettext

# This variable is not used (defined only for the translation with context)
_THEMES_TRANSLATED = (
    # Translators: name of the theme (in English: light / dark)
    pgettext('theme name for website', 'light'),
    # Translators: name of the theme (in English: light / dark)
    pgettext('theme name for website', 'dark'),
)


def theme(request):
    """Add theme variables in context."""
    user_theme = request.GET.get(
        'theme',
        request.COOKIES.get('theme', settings.THEMES[0]),
    )
    if user_theme not in settings.THEMES:
        user_theme = settings.THEMES[0]
    other_themes = [name for name in settings.THEMES if name != user_theme]
    return {
        'theme': user_theme,
        'other_themes': other_themes,
    }
