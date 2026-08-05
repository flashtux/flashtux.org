# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Some useful tags for link to files."""

import os

from django import template
from django.template.defaultfilters import filesizeformat
from django.utils.safestring import mark_safe
from django.utils.translation import gettext

from flashtux.common.path import files_path_join

# pylint: disable=invalid-name
register = template.Library()


@register.filter()
def linkfile(filename):
    """Return a link to a file with the size between parentheses."""
    path = files_path_join(filename)
    if os.path.exists(path):
        is_dir = os.path.isdir(path)
        base_path = os.path.basename(path) + ('/' if is_dir else '')
        result = f'<a href="/files/{filename}">{base_path}</a>'
        if os.path.isfile(path):
            result += f' ({filesizeformat(os.path.getsize(path))})'
        elif is_dir:
            result += f' ({gettext("directory")})'
    else:
        not_found = gettext('File not found')
        result = f'<span class="text-muted">{not_found}</span>'
    return mark_safe(result)


register.simple_tag(linkfile)
