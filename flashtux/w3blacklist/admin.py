# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Admin for w3blacklist."""

from django.contrib import admin

from flashtux.common.admin import FlashtuxAdmin
from flashtux.w3blacklist.models import Comment, Letter, Site

admin.site.register(Site, FlashtuxAdmin)
admin.site.register(Comment, FlashtuxAdmin)
admin.site.register(Letter, FlashtuxAdmin)
