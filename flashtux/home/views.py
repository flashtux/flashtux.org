# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Views for home."""

from sys import version as python_version

from django import __version__ as django_version
from django.shortcuts import render

from flashtux.home.models import Project


def projects(request):
    """Paginate list of news."""
    project_list = Project.objects.order_by('priority')
    return render(request, 'home/projects.html',
                  {'project_list': project_list})


def about(request, extra_info=False):
    """About FlashTux.org."""
    context = {}
    if extra_info:
        context.update({
            'extra_info': {
                'django': django_version,
                'python': python_version,
            },
        })
    return render(request, 'home/about.html', context)
