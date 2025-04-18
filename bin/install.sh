#!/bin/sh
#
# SPDX-FileCopyrightText: 1999-2025 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later
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

set -o errexit

DIR=$(cd "$(dirname "$0")"; pwd)

cd "$DIR/.."

echo ""
echo "--- Compiling messages"
./manage.py compilemessages

echo ""
echo "--- Creating database"
./manage.py migrate --run-syncdb

echo ""
echo "--- Loading fixtures in database"
./manage.py loaddata ./flashtux/fixtures/*.json

echo ""
echo "--- Install OK!"
echo ""
echo "--- You can run Django server with:  ./test.sh"
