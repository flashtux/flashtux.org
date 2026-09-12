# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Admin for news."""

from django.contrib import admin

from flashtux.common.admin import FlashtuxAdmin
from flashtux.news.models import Comment, Info

admin.site.register(Info, FlashtuxAdmin)
admin.site.register(Comment, FlashtuxAdmin)
