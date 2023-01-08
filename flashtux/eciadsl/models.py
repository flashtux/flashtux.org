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

"""Models for eciadsl."""

from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import gettext, gettext_lazy, pgettext_lazy
from django_countries import countries

from flashtux.common.i18n import i18n_autogen

MODEM_STATUS_CHOICES = (
    (0, gettext_lazy('Not supported')),
    (1, gettext_lazy('Maybe supported')),
    (2, gettext_lazy('Supported')),
)
MODEM_STATUS_TITLE = {
    0: pgettext_lazy('plural', 'Not supported'),
    1: pgettext_lazy('plural', 'Maybe supported'),
    2: pgettext_lazy('plural', 'Supported'),
}


class Modem(models.Model):
    """A modem."""
    manufacturer = models.CharField(max_length=256)
    modem = models.CharField(max_length=256)
    status = models.IntegerField(choices=MODEM_STATUS_CHOICES)
    drvmini = models.CharField(max_length=256, blank=True)
    vid1 = models.CharField(max_length=32, blank=True)
    pid1 = models.CharField(max_length=32, blank=True)
    vid2 = models.CharField(max_length=32, blank=True)
    pid2 = models.CharField(max_length=32, blank=True)
    country = models.CharField(max_length=256, blank=True)
    provider = models.CharField(max_length=256, blank=True)
    vpivci = models.CharField(max_length=256, blank=True)
    synchbin = models.CharField(max_length=256, blank=True)
    chipset = models.CharField(max_length=256, blank=True)
    synch_alt = models.CharField(max_length=16, blank=True)
    pppoeci_alt = models.CharField(max_length=256, blank=True)
    comment = models.TextField(blank=True)
    photo = models.CharField(max_length=256, blank=True)

    def __str__(self):
        """Return string representation of a Modem."""
        return f'{self.manufacturer} {self.modem} ({self.status_i18n()})'

    def status_i18n(self):
        """Return translated status."""
        return gettext(dict(MODEM_STATUS_CHOICES)[self.status])

    def status_title_i18n(self):
        """Return translated status for a title."""
        return gettext(MODEM_STATUS_TITLE[self.status])

    def country_string(self):
        """Return list of countries as string."""
        country_list1 = []
        for codes in self.country.split('/'):
            country_list2 = []
            for code in codes.split(','):
                code = code.upper()
                if code in countries.countries:
                    country_list2.append(gettext(countries.countries[code]))
                else:
                    country_list2.append(code)
            country_list1.append(', '.join(country_list2))
        return '\n'.join(country_list1)

    def provider_string(self):
        """Return list of providers as string."""
        return '\n'.join([
            ', '.join(prov.split(','))
            for prov in self.provider.split('/')
        ])

    def synchbin_string(self):
        """Return list of synch .bin as string."""
        return '\n'.join([
            ', '.join(synch.split(','))
            for synch in self.synchbin.split('/')
        ])

    def comment_i18n(self):
        """Return translated comment."""
        return gettext(self.comment) if self.comment else ''


def handler_modem_saved(sender, **kwargs):
    """Generate code to translate modems."""
    # pylint: disable=unused-argument
    strings = []
    for modem in Modem.objects.order_by('manufacturer', 'modem'):
        if modem.comment:
            strings.append(
                (
                    modem.comment,
                    f'comment for modem {modem.manufacturer} {modem.modem}',
                )
            )
    i18n_autogen('eciadsl', 'modem', strings)


post_save.connect(handler_modem_saved, sender=Modem)
