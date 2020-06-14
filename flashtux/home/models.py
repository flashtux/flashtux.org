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

"""Models for home."""

from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext

from flashtux.common.i18n import i18n_autogen


class Project(models.Model):
    """A FlashTux project."""
    name = models.CharField(max_length=64)
    start_date = models.DateField()
    stable_version = models.CharField(max_length=32, blank=True)
    stable_date = models.DateField(blank=True, null=True)
    devel_version = models.CharField(max_length=32, blank=True)
    description = models.TextField()
    license = models.CharField(max_length=32)
    support = models.CharField(max_length=1024, blank=True)
    page = models.CharField(max_length=1024)
    website = models.CharField(max_length=1024, blank=True)
    repository = models.CharField(max_length=1024, blank=True)
    screenshot = models.CharField(max_length=1024, blank=True)
    priority = models.IntegerField(default=0)

    def __str__(self):
        """Return string representation of a Project."""
        return f'{self.name} ({self.priority})'

    def description_i18n(self):
        """Return translated text."""
        return ugettext(self.description)

    class Meta:
        """Meta class for Project."""
        ordering = ['priority']


def handler_project_saved(sender, **kwargs):
    """Generate code to translate projects."""
    # pylint: disable=unused-argument
    strings = []
    for project in Project.objects.order_by('priority'):
        strings.append(project.description)
        strings.append(project.support)
    i18n_autogen('home', 'project', strings)


post_save.connect(handler_project_saved, sender=Project)
