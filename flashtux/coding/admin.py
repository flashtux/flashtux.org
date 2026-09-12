# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Admin for programs."""

from django.contrib import admin

from flashtux.coding.models import Program
from flashtux.common.admin import FlashtuxAdmin

admin.site.register(Program, FlashtuxAdmin)
