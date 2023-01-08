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

"""Models for programs."""

from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import gettext

from flashtux.common.i18n import i18n_autogen


class Program(models.Model):
    """A program."""
    name = models.CharField(max_length=64, primary_key=True)
    category = models.CharField(max_length=64)
    operating_system = models.CharField(max_length=256)
    prog_language = models.CharField(max_length=64)
    shortdesc = models.CharField(max_length=1024)
    description = models.TextField()
    output = models.TextField(blank=True)
    images = models.CharField(max_length=1024, blank=True)
    filename = models.CharField(max_length=256)
    filename_description = models.CharField(max_length=1024)
    author = models.CharField(max_length=256)
    email = models.CharField(max_length=256)

    def __str__(self):
        """Return string representation of a Program."""
        return f'[{self.category}] {self.name}: {self.shortdesc}'

    def prog_language_i18n(self):
        """Return translated programming language."""
        return gettext(self.prog_language)

    def shortdesc_i18n(self):
        """Return translated short description."""
        return gettext(self.shortdesc)

    def description_i18n(self):
        """Return translated description."""
        return gettext(self.description.replace('\r\n', '\n'))

    def images_list(self):
        """Return a list of images."""
        return self.images.split(',')

    class Meta:
        """Meta class for Site."""
        ordering = ['category', 'name']


def handler_program_saved(sender, **kwargs):
    """Generate code to translate programs."""
    # pylint: disable=unused-argument
    strings_categ = []
    strings_lang = []
    strings = []
    for prog in Program.objects.order_by('category', 'name'):
        strings_categ.append(prog.category.capitalize())
        strings_lang.append((prog.prog_language, 'Programming language'))
        strings.append((prog.shortdesc,
                        f'short description for program "{prog.name}"'))
        strings.append((prog.description,
                        f'description for program "{prog.name}"'))
        strings.append((prog.filename_description,
                        f'filename description for program "{prog.name}"'))
    i18n_autogen('coding', 'program', strings_categ + strings_lang + strings)


post_save.connect(handler_program_saved, sender=Program)
