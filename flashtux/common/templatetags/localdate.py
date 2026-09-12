# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Some useful tags for localized dates."""

from datetime import date, datetime

from django import template
from django.conf import settings
from django.utils import dateformat, timezone
from django.utils.html import format_html
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
            value = date.fromisoformat(value)
    elif fmt_lower == 'date_year_month':
        date_fmt = gettext(settings.DATE_YEAR_MONTH_FORMAT)
        if not isinstance(value, (date, datetime)):
            # "YYYY-MM" is not supported by date.fromisoformat()
            value = date.fromisoformat(f'{value}-01')
    elif fmt_lower == 'datetime':
        date_fmt = gettext(settings.DATETIME_FORMAT)
        if not isinstance(value, (date, datetime)):
            value = datetime.strptime(value, '%Y-%m-%d %H:%M').replace(
                tzinfo=timezone.get_current_timezone(),
            )
    else:
        date_fmt = fmt
    date_value = dateformat.format(value, date_fmt)
    if fmt[0].isupper():
        date_value = date_value.capitalize()
    date_iso = value.isoformat()
    return format_html('<time datetime="{}">{}</time>', date_iso, date_value)
