# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

all: check

check: gettext lint

lint: flake8 pylint

gettext:
	poexam check --file-stats --rule-stats

flake8:
	flake8 . --count --max-line-length=88 --select=E9,F63,F7,F82 --exclude=migrations --show-source --statistics
	flake8 . --count --max-line-length=88 --exclude=migrations --exit-zero --max-complexity=10 --statistics

pylint:
	pylint --load-plugins pylint_django --disable=django-not-configured --ignore=migrations flashtux
