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

"""Models for image."""

from django.db import models

from flashtux.news.models import SECTIONS_CHOICES


class Image(models.Model):
    """An image."""
    section = models.CharField(max_length=32, choices=SECTIONS_CHOICES)
    category = models.CharField(max_length=256)
    filename = models.CharField(max_length=256)
    comment = models.TextField(blank=True)
    priority = models.IntegerField(default=0)

    def __str__(self):
        """Return string representation of an Image."""
        return (f'{self.section} ({self.category}): '
                f'{self.filename} ({self.priority})')

    class Meta:
        """Meta class for Image."""
        ordering = ['section', 'category', 'priority']
