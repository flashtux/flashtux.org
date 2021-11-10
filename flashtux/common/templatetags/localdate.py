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

"""Some useful tags for localized dates."""

from datetime import date, datetime

from django import template
from django.conf import settings
from django.utils import dateformat
from django.utils.safestring import mark_safe
from django.utils.translation import gettext

# pylint: disable=invalid-name
register = template.Library()


@register.filter()
def localdate(value, fmt='date'):
    """
    Format date with localized date/time format.
    If fmt == "date", the localized date format is used.
    If fmt == "datetime", the localized date/fime format is used.
    Another fmt it is used as-is.
    """
    fmt_lower = fmt.lower()
    if fmt_lower == 'date':
        date_fmt = gettext(settings.DATE_FORMAT)
        if not isinstance(value, (date, datetime)):
            value = datetime.strptime(value, '%Y-%m-%d').date()
    elif fmt_lower == 'date_year_month':
        date_fmt = gettext(settings.DATE_YEAR_MONTH_FORMAT)
        if not isinstance(value, (date, datetime)):
            value = datetime.strptime(value, '%Y-%m').date()
    elif fmt_lower == 'datetime':
        date_fmt = gettext(settings.DATETIME_FORMAT)
        if not isinstance(value, (date, datetime)):
            value = datetime.strptime(value, '%Y-%m-%d %H:%M')
    else:
        date_fmt = fmt
    date_value = dateformat.format(value, date_fmt)
    if fmt[0].isupper():
        date_value = date_value.capitalize()
    date_iso = value.isoformat()
    return mark_safe(f'<time datetime="{date_iso}">{date_value}</time>')
