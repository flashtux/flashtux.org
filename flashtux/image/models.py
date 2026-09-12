# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

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
        ordering = ('section', 'category', 'priority')
