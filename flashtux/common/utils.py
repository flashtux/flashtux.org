# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Some useful functions."""


def truncate_content(content, length=64):
    """Return the truncated content."""
    if len(content) > length:
        return content[:64] + '(…)'
    return content
