#
# Copyright (C) 1999-2022 Sébastien Helleu <flashcode@flashtux.org>
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

"""FlashTux feeds."""

from django.contrib.syndication.views import Feed

from flashtux.news.models import Info


class LatestNewsFeed(Feed):
    """Feed with latest news."""
    title = 'FlashTux news'
    description = title
    link = '/news/'

    def get_object(self, request, *args, **kwargs):
        # pylint: disable=attribute-defined-outside-init
        self.request = request
        self.section = kwargs.get('section')

    def items(self):
        """Return items with date in the past."""
        infos = Info.objects.all()
        if self.section:
            infos = infos.filter(section=self.section)
        return infos.order_by('-date')[:10]

    def item_link(self, item):
        """Return link to item by using the domain sent in the request."""
        return (f'{self.request.scheme}://{self.request.get_host()}'
                f'/news/{item.pk}')

    def item_pubdate(self, item):
        """Return idem date."""
        # pylint: disable=no-self-use
        return item.date
