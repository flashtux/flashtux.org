# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

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
