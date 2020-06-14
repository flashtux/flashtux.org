# -*- coding: utf-8 -*-
#
# Copyright (C) 1999-2020 Sébastien Helleu <flashcode@flashtux.org>
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

"""Some useful tags for link to files."""

import os

from django import template
from django.template.defaultfilters import filesizeformat
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext

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
            result += ' (%s)' % filesizeformat(os.path.getsize(path))
        elif is_dir:
            result += ' (%s)' % ugettext('directory')
    else:
        result = '<span class="text-muted">%s</span>' % (
            ugettext('File not found'))
    return mark_safe(result)


register.simple_tag(linkfile)
