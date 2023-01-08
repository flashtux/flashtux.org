#
# Copyright (C) 1999-2023 Sébastien Helleu <flashcode@flashtux.org>
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

"""Views for w3blacklist."""

from django.shortcuts import render, get_object_or_404

from flashtux.w3blacklist.models import Site, Letter


def sites(request, status=None, site_id=None):
    """List of sites."""
    data = {
        'status': status,
    }
    # general counts
    count_blacklist = Site.objects.filter(status=2).count()
    count_fixed = Site.objects.filter(status=3).count()
    count_approval = Site.objects.filter(status=1).count()
    count_waiting_response = (Site.objects.filter(status=1)
                              .exclude(sentmail='').count())
    data.update({
        'count_blacklist': count_blacklist,
        'count_fixed': count_fixed,
        'count_approval': count_approval,
        'count_pending_approval': count_approval - count_waiting_response,
        'count_waiting_response': count_waiting_response,
    })
    # list of sites
    if site_id:
        site = get_object_or_404(Site, pk=site_id)
        comments = site.comment_set.all().order_by('date')
        data['site'] = site
        data['comments'] = comments
    else:
        site_list = Site.objects.order_by('-date', '-id')
        if status == 'blacklist':
            site_list = site_list.filter(status=2)
        elif status == 'fixed':
            site_list = site_list.filter(status=3)
        data['sites'] = site_list
    return render(request, 'w3blacklist/sites.html', data)


def letters(request):
    """List of letters."""
    letter_list = Letter.objects.all()
    return render(request, 'w3blacklist/letters.html',
                  {'letters': letter_list})
