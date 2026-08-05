# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Views for programs."""

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils.translation import gettext

from flashtux.coding.models import Program


def programs(request, category=None, name=None):
    """List of programs."""
    categories = (Program.objects.distinct('category').order_by('category')
                  .values_list('category', flat=True))
    categories = [
        (categ, gettext(categ.capitalize()))
        for categ in categories
    ]
    data = {
        'categories': categories,
        'category': category,
        'name': name,
    }
    if name:
        data['program'] = get_object_or_404(Program, name=name)
    else:
        prog_list = get_list_or_404(Program, category=category)
        data['programs'] = prog_list
    return render(request, 'coding/programs.html', data)
