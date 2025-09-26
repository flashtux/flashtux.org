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

"""URLs for flashtux.org."""

# pylint: disable=invalid-name

from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path
from django.contrib import admin
from django.views.generic.base import RedirectView

from flashtux.common.views import TextTemplateView
from flashtux.home.views import projects, about
from flashtux.news.feeds import LatestNewsFeed
from flashtux.news.models import RE_SECTIONS
from flashtux.news.views import news_section, form_comment

URL_ABOUT_EXTRA = getattr(settings, 'URL_ABOUT_EXTRA', 'extra')

# admin
admin.autodiscover()

urlpatterns = [
    # favicon.ico
    path('favicon.ico',
         RedirectView.as_view(url=f'{settings.MEDIA_URL}images/favicon.png',
                              permanent=True)),

    # admin
    path(f'{settings.ADMIN_PAGE}/doc/',
         include('django.contrib.admindocs.urls')),
    path(f'{settings.ADMIN_PAGE}/', admin.site.urls),

    # set language
    path('i18n/', include('django.conf.urls.i18n')),

    # main FlashTux URLs
    path('', news_section, name='home_news'),
    re_path(rf'^(?P<section>{RE_SECTIONS})/$', news_section, name='news'),
    re_path(rf'^info/(?P<section>{RE_SECTIONS})/(?P<info_id>[0-9]*)/$',
            news_section, name='info'),
    re_path(rf'^info/reply/(?P<section>{RE_SECTIONS})/(?P<info_id>[0-9]*)-'
            rf'(?P<comment_relative_id>[0-9]*)/$',
            form_comment, name='info_reply'),
    path('projects/', projects, name='home_projects'),
    path('about/', about, name='home_about'),
    path(f'about/{URL_ABOUT_EXTRA}/', about, {'extra_info': True}),
    path('eciadsl/', include('flashtux.eciadsl.urls')),
    path('weewm/', include('flashtux.weewm.urls')),
    path('w3blacklist/', include('flashtux.w3blacklist.urls')),
    path('gmemo/', include('flashtux.gmemo.urls')),
    path('flashtris/', include('flashtux.flashtris.urls')),
    path('coding/', include('flashtux.coding.urls')),
    path('games/', include('flashtux.games.urls')),

    # feeds
    path('feeds/news/', LatestNewsFeed(), name='feeds_news'),
    re_path(rf'^feeds/news/(?P<section>{RE_SECTIONS})/$',
            LatestNewsFeed(), name='feeds_news_section'),

    # files and media
    path('files', RedirectView.as_view(url='/files/')),
    path('media', RedirectView.as_view(url='/media/')),

    # robots.txt
    path('robots.txt', TextTemplateView.as_view(template_name='robots.txt')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += static(
        settings.FILES_URL,
        document_root=settings.FILES_ROOT,
        show_indexes=True,
    )
