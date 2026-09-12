# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""FlashTux feeds."""

from django.contrib.syndication.views import Feed

from flashtux.news.models import Info


class LatestNewsFeed(Feed):
    """Feed with latest news."""
    title = 'FlashTux news'
    description = title
    link = '/news/'

    def get_object(self, request, *args, **kwargs):
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
        return item.date
