#!/bin/sh
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

#
# Bump a project version in database:
#  1. set stable version + date (today)
#  2. set devel version
#
# Syntax:
#   ./bump_project_version.sh <project> <stable> [<devel>]
#
# Examples:
#   ./bump_project_version.sh WeeChat 4.0.0 4.1.0-dev
#   ./bump_project_version.sh WeeChat 4.0.1
#

set -o errexit

DIR=$(cd "$(dirname "$0")"; pwd)

if [ $# -lt 2 ]; then
    echo "Syntax: $0 <project> <stable> [<devel>]"
    exit 1
fi

PROJECT="$1"
STABLE="$2"
DEVEL=""
if [ $# -gt 2 ]; then
    DEVEL="$3"
fi

if [ -n "${DEVEL}" ]; then
    echo "Setting in project ${PROJECT}: stable=${STABLE}, devel=${DEVEL}"
else
    echo "Setting in project ${PROJECT}: stable=${STABLE}"
fi

"${DIR}/../manage.py" shell <<EOF
from datetime import date
from flashtux.home.models import Project
project = Project.objects.get(name="${PROJECT}")
project.stable_date = date.today()
project.stable_version = "${STABLE}"
if "${DEVEL}":
    project.devel_version = "${DEVEL}"
project.save()
EOF
