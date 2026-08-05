# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Admin for home."""

from django.contrib import admin

from flashtux.common.admin import FlashtuxAdmin
from flashtux.home.models import Project

admin.site.register(Project, FlashtuxAdmin)
