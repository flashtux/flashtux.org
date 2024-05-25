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
