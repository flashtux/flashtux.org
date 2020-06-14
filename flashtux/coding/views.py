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

"""Views for programs."""

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils.translation import ugettext

from flashtux.coding.models import Program


def programs(request, category=None, name=None):
    """List of programs."""
    categories = (Program.objects.distinct('category').order_by('category')
                  .values_list('category', flat=True))
    categories = [
        (categ, ugettext(categ.capitalize()))
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
