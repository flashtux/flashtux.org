#
# Copyright (C) 1999-2024 Sébastien Helleu <flashcode@flashtux.org>
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

"""Some useful views."""

from django.shortcuts import render
from django.utils.translation import gettext
from django.views.generic import TemplateView


class TextTemplateView(TemplateView):
    """View for a plain text file."""
    def render_to_response(self, context, **response_kwargs):
        response_kwargs['content_type'] = 'text/plain'
        return super().render_to_response(context, **response_kwargs)


class DownloadView(TemplateView):
    """A download view."""
    def get_context_data(self, **kwargs):
        return {
            'version': kwargs.get('version') or 'stable',
        }


def doc(request, section, versions, languages, other_docs=None):
    """Documentation view."""
    formats = (
        ('html', 'HTML'),
        ('pdf', 'PDF'),
        ('txt', gettext('Text')),
        ('texi', 'Texinfo'),
    )
    return render(
        request,
        f'{section}/doc.html',
        {
            'section': section,
            'versions': versions,
            'formats': formats,
            'languages': languages,
            'other_docs': other_docs,
        }
    )


def faq(request, section, versions, languages):
    """Documentation view."""
    formats = (
        ('txt', gettext('Text')),
    )
    return render(
        request,
        f'{section}/faq.html',
        {
            'section': section,
            'versions': versions,
            'formats': formats,
            'languages': languages,
        }
    )
