# SPDX-FileCopyrightText: 2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""URLs for "weechat" menu."""

from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    # legacy links
    path(
        "download/",
        RedirectView.as_view(
            url="https://weechat.org/download/",
            permanent=True,
        ),
    ),
]
