# -*- coding: utf-8 -*-
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

"""Models for news."""

import re

from django import forms
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext, ugettext_lazy

from flashtux.common.forms import (
    CharField,
    EmailField,
    Form,
    Html5EmailInput,
    TestField,
)
from flashtux.common.i18n import i18n_autogen

SECTIONS = (
    'home',
    'weechat',
    'eciadsl',
    'weewm',
    'w3blacklist',
    'gmemo',
    'flashtris',
    'coding',
    'games',
)
SECTIONS_CHOICES = [
    (section, section)
    for section in SECTIONS
]
RE_SECTIONS = '(%s)' % '|'.join(SECTIONS)

PATTERN_TITLE_VERSION = re.compile('(Version) ([0-9.a-z-]*)$')


class Info(models.Model):
    """A FlashTux info."""
    section = models.CharField(max_length=32, choices=SECTIONS_CHOICES)
    date = models.DateTimeField()
    title = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    text = models.TextField()

    def __str__(self):
        """Return string representation of an Info."""
        return '%s, %s: %s' % (
            self.date.strftime('%Y-%m-%d %H:%M'),
            self.section,
            self.title,
        )

    def __unicode__(self):  # python 2.x
        """Return unicode representation of an Info."""
        return self.__str__()

    def section_i18n(self):
        """Return the translated section, for display."""
        section_display = {
            'home': 'FlashTux',
            'weechat': 'WeeChat',
            'eciadsl': 'EciAadsl',
            'weewm': 'WeeWM',
            'w3blacklist': 'W3BlackList',
            'gmemo': 'Gmemo',
            'flashtris': 'FlashTris',
            'coding': ugettext('Coding'),
            'games': ugettext('Games'),
        }
        return section_display[self.section]

    def title_i18n(self):
        """Return translated title."""
        match = PATTERN_TITLE_VERSION.match(self.title)
        if match:
            # if the title is "Version x.y.z", translate only "Version"
            return '%s %s' % (ugettext(match.group(1)), match.group(2))
        else:
            return ugettext(self.title)

    def text_i18n(self):
        """Return translated text."""
        return ugettext(self.text.replace('\r\n', '\n'))

    def date_title_url(self):
        """Return date+title to include in URL."""
        return '%04d%02d%02d-%02d%02d-%s' % (
            self.date.year, self.date.month, self.date.day,
            self.date.hour, self.date.min,
            re.sub(' +', '-',
                   re.sub('[^ a-zA-Z0-9.]', ' ',
                          self.title).strip()))

    class Meta:
        """Meta class for Info."""
        ordering = ['-date']


class Comment(models.Model):
    """A FlashTux comment on info."""
    comment_relative = models.ForeignKey("Comment", on_delete=models.CASCADE,
                                         null=True)
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    date = models.DateTimeField()
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256, blank=True)
    title = models.CharField(max_length=256)
    content = models.TextField()

    def __str__(self):
        """Return string representation of a Comment."""
        return '%s, %s: %s' % (
            self.date.strftime('%Y-%m-%d %H:%M'),
            self.info.section,
            self.content_truncated(),
        )

    def __unicode__(self):  # python 2.x
        """Return unicode representation of a Comment."""
        return self.__str__()

    def content_truncated(self, length=64):
        """Return the truncated content."""
        if len(self.content) > length:
            return self.content[:64] + u'(…)'
        return self.content

    class Meta:
        """Meta class for Comment."""
        ordering = ['-date']


class CommentFormAdd(Form):
    """Form to add a script."""
    required_css_class = 'required'
    title = CharField(
        max_length=256,
        label=ugettext_lazy('Title'),
        help_text=ugettext_lazy('The comment title.'),
    )
    content = CharField(
        max_length=1024,
        label=ugettext_lazy('Comment'),
        help_text=ugettext_lazy('Your comment.'),
        widget=forms.Textarea(attrs={'rows': '6', 'autofocus': True}),
    )
    name = CharField(
        max_length=256,
        label=ugettext_lazy('Your name or nick'),
        help_text=ugettext_lazy('Displayed above the comment.'),
    )
    email = EmailField(
        max_length=256,
        label=ugettext_lazy('Your e-mail'),
        help_text=ugettext_lazy('Optional, never displayed.'),
        required=False,
        widget=Html5EmailInput(),
    )
    test = TestField(
        max_length=64,
        label=ugettext_lazy('Are you a spammer?'),
        help_text=ugettext_lazy('Enter "no" if you are not a spammer.'),
    )

    def __init__(self, *args, **kwargs):
        info = kwargs.pop('ctx_info', None)
        comment_relative = kwargs.pop('ctx_comment_relative', None)
        super(CommentFormAdd, self).__init__(*args, **kwargs)
        self.label_suffix = ''
        if comment_relative:
            title = comment_relative.title
            if not title.startswith('Re: '):
                title = 'Re: %s' % title
            self.fields['title'].initial = title
        elif info:
            self.fields['title'].initial = 'Re: %s' % info.title_i18n()


def handler_info_saved(sender, **kwargs):
    """Generate code to translate news."""
    strings = []
    for info in Info.objects.order_by('-date'):
        translators = info.__unicode__()
        match = PATTERN_TITLE_VERSION.match(info.title)
        if match:
            # if the title is "Version x.y.z", translate only "Version"
            strings.append((match.group(1), translators))
        else:
            strings.append((info.title, translators))
        if info.text:
            strings.append((info.text, translators))
    i18n_autogen('news', 'info', strings)


post_save.connect(handler_info_saved, sender=Info)
