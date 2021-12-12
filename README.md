# FlashTux.org

[![Build Status](https://github.com/flashtux/flashtux.org/workflows/CI/badge.svg)](https://github.com/flashtux/flashtux.org/actions?query=workflow%3A%22CI%22)

FlashTux.org is the website for FlashTux, the home of free projects for free OS.

Homepage: https://flashtux.org/

## Install

### Dependencies

Following packages are **required**:

- python ≥ 3.6
- python-django ≥ 2.0
- python-tz
- python-django-countries
- PostgreSQL.

### Deploy

Run the install script:

```
$ ./bin/install.sh
```

Run Django server:

```
$ ./test.sh
```

And just point your browser on http://127.0.0.1:8000/, that's all!

Important: default settings can be used for testing purposes but must be overridden
for production, see the file [settings_local.template](flashtux/settings_local.template) for more information.

## Authors

- Design/code:
  - Sébastien Helleu (FlashCode)

## Copyright

Copyright © 1999-2021 [Sébastien Helleu](https://github.com/flashcode)

This file is part of FlashTux.org.

FlashTux.org is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

FlashTux.org is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with FlashTux.org.  If not, see <https://www.gnu.org/licenses/>.
