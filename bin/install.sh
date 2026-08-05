#!/bin/sh
#
# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

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
