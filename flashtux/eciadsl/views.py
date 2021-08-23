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

"""Views for EciAdsl."""

from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy

from flashtux.common.views import (
    doc as view_doc,
    faq as view_faq,
)
from flashtux.eciadsl.models import Modem


def doc(request):
    """EciAdsl documentation."""
    versions = (
        ('eciadsl_install',
         gettext_lazy('EciAdsl installation guide'),
         'v0.12'),
        ('eciadsl-devel_install',
         gettext_lazy('EciAdsl installation guide'),
         gettext_lazy('development version')),
    )
    languages = (
        ('fr', gettext_lazy('French')),
        ('en', gettext_lazy('English')),
        ('it', gettext_lazy('Italian')),
        ('es', gettext_lazy('Spanish')),
        ('de', gettext_lazy('German')),
        ('tr', gettext_lazy('Turkish')),
    )
    other_docs = (
        (['fr', 'en'],
         '/files/eciadsl/doc/eciadsl-mdk10.txt',
         gettext_lazy('EciAdsl installation with Mandrake 10 and kernel '
                      '2.6.x')),
        (['fr', 'en'],
         '/files/download/eciadsl/beta/',
         gettext_lazy('Instructions for 2.6.x kernels patch')),
        (['fr', 'en'],
         '/files/eciadsl/doc/eciadsl-on-openbsd.txt',
         gettext_lazy('EciAdsl installation on *BSD')),
        (['fr'],
         '/files/eciadsl/doc/eciadsl-free-degroupe.txt',
         gettext_lazy('EciAdsl config with "Free dégroupé" (France only)')),
        (['fr', 'en'],
         '/files/eciadsl/doc/eciadsl-avangard.txt',
         gettext_lazy('EciAdsl with Avangard provider (Russia)')),
        (['fr', 'en'],
         '/files/eciadsl/doc/eciadsl-noapic.txt',
         gettext_lazy('EciAdsl and APIC problem')),
        (['en'],
         '/files/eciadsl/doc/dsl200.html',
         gettext_lazy('EciAdsl with DSL-200 B1 modem and TPG '
                      '(australian ISP)')),
        (['en'],
         '/files/eciadsl/doc/eciadsl_hotplug_en.html',
         gettext_lazy('EciAdsl with hotplug')),
    )
    return view_doc(request, 'eciadsl', versions, languages,
                    other_docs=other_docs)


def faq(request):
    """EciAdsl FAQ."""
    versions = (
        ('TROUBLESHOOTING', gettext_lazy('EciAdsl FAQ'), ''),
    )
    languages = (
        ('fr', gettext_lazy('French')),
        ('en', gettext_lazy('English')),
        ('it', gettext_lazy('Italian')),
        ('pt', gettext_lazy('Portuguese')),
        ('es', gettext_lazy('Spanish')),
    )
    return view_faq(request, 'eciadsl', versions, languages)


def modems(request, status=None, modem_id=None):
    """List of modems."""
    # count of supported modems by status
    # result is a dict like this: {'0': 21, '1': 3, '2': 65, 'all': 89}
    count_list = (Modem.objects.values('status')
                  .annotate(total=Count('status')).order_by('status'))
    count = {
        str(total['status']): total['total']
        for total in count_list
    }
    count['all'] = sum(count.values())
    # list of modems
    if modem_id:
        modem = get_object_or_404(Modem, pk=modem_id)
        modem_list = [modem]
    else:
        modem_list = Modem.objects.order_by('-status', 'manufacturer',
                                            'modem')
        if status == 'supported':
            modem_list = modem_list.filter(status=2)
        elif status == 'maybe':
            modem_list = modem_list.filter(status=1)
        elif status == 'notsupported':
            modem_list = modem_list.filter(status=0)
    return render(
        request,
        'eciadsl/modems.html',
        {
            'status': status,
            'count': count,
            'modems': modem_list,
        }
    )
