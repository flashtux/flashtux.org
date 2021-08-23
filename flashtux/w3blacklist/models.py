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

"""Models for w3blacklist."""

from collections import OrderedDict
import re

from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import gettext, gettext_lazy

from flashtux.common.utils import truncate_content
from flashtux.common.i18n import i18n_autogen

SITE_STATUS_CHOICES = (
    # Translators: status of a w3blacklist site
    (0, gettext_lazy('rejected')),
    # Translators: status of a w3blacklist site
    (1, gettext_lazy('waiting for approval')),
    # Translators: status of a w3blacklist site
    (2, gettext_lazy('blacklisted')),
    # Translators: status of a w3blacklist site
    (3, gettext_lazy('fixed')),
)
SITE_SEVERITY_CHOICES = (
    (1, gettext_lazy('display issues')),
    (2, gettext_lazy('partially broken')),
    (3, gettext_lazy('entirely broken')),
)


class Site(models.Model):
    """A w3blacklist site."""
    status = models.IntegerField(choices=SITE_STATUS_CHOICES)
    lang = models.CharField(max_length=32)
    website = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    contact = models.CharField(max_length=256, blank=True)
    shortdesc = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    internet_explorer = models.CharField(max_length=1, blank=True)
    konqueror = models.CharField(max_length=1, blank=True)
    chrome = models.CharField(max_length=1, blank=True)
    mozilla = models.CharField(max_length=1, blank=True)
    opera = models.CharField(max_length=1, blank=True)
    win = models.CharField(max_length=1, blank=True)
    mac = models.CharField(max_length=1, blank=True)
    unix = models.CharField(max_length=1, blank=True)
    severity = models.IntegerField(choices=SITE_SEVERITY_CHOICES)
    sentmail = models.TextField(blank=True)
    recvmail = models.TextField(blank=True)
    date = models.DateField()
    date_update = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=256, blank=True)
    email = models.CharField(max_length=256, blank=True)

    def __str__(self):
        """Return string representation of a Site."""
        return (f'{self.date}: {self.website} - '
                f'{self.url} ({self.status_i18n()})')

    def status_i18n(self):
        """Return translated status."""
        return gettext(dict(SITE_STATUS_CHOICES)[self.status])

    def shortdesc_i18n(self):
        """Return translated short description."""
        if self.shortdesc:
            return gettext(self.shortdesc.replace('\r\n', '\n'))
        return ''

    def description_i18n(self):
        """Return translated description."""
        if self.description:
            return gettext(self.description.replace('\r\n', '\n'))
        return ''

    def severity_x(self):
        """Return the severity as a string of N "x"."""
        return 'x' * self.severity

    def severity_i18n(self):
        """Return the translated severity description."""
        return gettext(dict(SITE_SEVERITY_CHOICES)[self.severity])

    def browsers(self):
        """Return dict with browsers compatibility."""
        return OrderedDict([
            ('IE', self.internet_explorer != '1'),
            ('Firefox', self.mozilla != '1'),
            ('Chrome', self.chrome != '1'),
            ('Konqueror', self.konqueror != '1'),
            ('Opera', self.opera != '1'),
        ])

    def operating_system(self):
        """Return dict with OS compatibility."""
        return OrderedDict([
            ('Windows', self.win != '1'),
            ('Linux', self.unix != '1'),
            ('macOS', self.mac != '1'),
        ])

    def list_sentmail(self):
        """Return a list of dates for "sentmail"."""
        if not self.sentmail:
            return []
        return [
            date.strip()
            for date in self.sentmail.split(',')
        ]

    def list_recvmail(self):
        """Return a list of dates for "recvmail"."""
        if not self.recvmail:
            return []
        return [
            date.strip()
            for date in self.recvmail.split(',')
        ]

    class Meta:
        """Meta class for Site."""
        ordering = ['-date', 'website']


class Comment(models.Model):
    """A w3blacklist site comment."""
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateField()
    name = models.CharField(max_length=256)

    def __str__(self):
        """Return string representation of a Comment."""
        str_name = self.name or '(anonymous)'
        return (f'{self.date}, {str_name}: {truncate_content(self.content)} '
                f'({self.site.url}, {self.site.status_i18n()})')


class Letter(models.Model):
    """A w3blacklist letter."""
    description = models.CharField(max_length=1024)
    content = models.TextField()
    priority = models.IntegerField(default=0)

    def __str__(self):
        """Return string representation of a Letter."""
        return (f'{self.description}: {self.content_truncated()} '
                f'({self.priority})')

    def description_i18n(self):
        """Return translated description."""
        return gettext(self.description)

    def content_i18n(self):
        """Return translated content, with HTML tags for variable text."""
        translated = gettext(self.content.replace('\r\n', '\n'))
        return re.sub(r'\[\[(.+?)\]\]',
                      r'<span class="highlight">\1</span>',
                      translated)

    def content_truncated(self, length=64):
        """Return the truncated content."""
        if len(self.content) > length:
            return self.content[:64] + '(…)'
        return self.content

    class Meta:
        """Meta class for Letter."""
        ordering = ['priority']


def handler_site_saved(sender, **kwargs):
    """Generate code to translate sites."""
    # pylint: disable=unused-argument
    strings = []
    for site in Site.objects.order_by('-date', 'website'):
        if site.status not in (2, 3):
            # status is not blacklisted or fixed
            continue
        strings.append(
            (
                site.shortdesc,
                f'short description for site {site.website} ({site.url})',
            )
        )
        if site.description:
            strings.append(
                (
                    site.description,
                    f'description for site {site.website} ({site.url})',
                )
            )
    i18n_autogen('w3blacklist', 'site', strings)


def handler_letter_saved(sender, **kwargs):
    """Generate code to translate letters."""
    # pylint: disable=unused-argument
    strings = []
    for letter in Letter.objects.order_by('priority'):
        strings.append((letter.content, f'Letter: {letter.description}'))
    i18n_autogen('w3blacklist', 'letter', strings)


post_save.connect(handler_site_saved, sender=Site)
post_save.connect(handler_letter_saved, sender=Letter)
