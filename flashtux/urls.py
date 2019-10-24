# -*- coding: utf-8 -*-
#
# Copyright (C) 1999-2019 Sébastien Helleu <flashcode@flashtux.org>
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

"""URLs for flashtux.org."""

# pylint: disable=invalid-name

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView, TemplateView

from flashtux.common.views import TextTemplateView
from flashtux.home.views import projects, about
from flashtux.news.feeds import LatestNewsFeed
from flashtux.news.models import RE_SECTIONS
from flashtux.news.views import news_section, form_comment

URL_ABOUT_EXTRA = getattr(settings, 'URL_ABOUT_EXTRA', 'extra')

# admin
admin.autodiscover()

urlpatterns = [
    # admin
    url(r'^%s/doc/' % settings.ADMIN_PAGE,
        include('django.contrib.admindocs.urls')),
    url(r'^%s/' % settings.ADMIN_PAGE, admin.site.urls),

    # set language
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # main FlashTux URLs
    url(r'^$', news_section, name='home_news'),
    url(r'^(?P<section>%s)/$' % RE_SECTIONS,
        news_section, name='news'),
    url(r'^info/(?P<section>%s)/(?P<info_id>[0-9]*)/$' % RE_SECTIONS,
        news_section, name='info'),
    url(r'^info/reply/(?P<section>%s)/(?P<info_id>[0-9]*)-'
        r'(?P<comment_relative_id>[0-9]*)/$' % RE_SECTIONS,
        form_comment, name='info_reply'),
    url(r'^projects/$', projects, name='home_projects'),
    url(r'^about/$', about, name='home_about'),
    url(r'^about/%s/$' % URL_ABOUT_EXTRA, about, {'extra_info': True}),
    url(r'^donate/$',
        TemplateView.as_view(template_name='home/donate.html'),
        name='home_donate'),
    url(r'^eciadsl/', include('flashtux.eciadsl.urls')),
    url(r'^weewm/', include('flashtux.weewm.urls')),
    url(r'^w3blacklist/', include('flashtux.w3blacklist.urls')),
    url(r'^gmemo/', include('flashtux.gmemo.urls')),
    url(r'^flashtris/', include('flashtux.flashtris.urls')),
    url(r'^coding/', include('flashtux.coding.urls')),
    url(r'^games/', include('flashtux.games.urls')),

    # feeds
    url(r'^feeds/news/$', LatestNewsFeed(), name='feeds_news'),
    url(r'^feeds/news/(?P<section>%s)/$' % RE_SECTIONS,
        LatestNewsFeed(), name='feeds_news_section'),

    # files and media
    url('^files$', RedirectView.as_view(url='/files/')),
    url('^media$', RedirectView.as_view(url='/media/')),

    # robots.txt
    url(r'^robots\.txt$',
        TextTemplateView.as_view(template_name='robots.txt')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.FILES_URL,
                          document_root=settings.FILES_ROOT)
