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

"""URLs for "flashtris" menu."""

# pylint: disable=invalid-name, no-value-for-parameter

from django.urls import path
from django.views.generic.base import TemplateView

from flashtux.image.views import images

urlpatterns = [
    path('screenshots/', images,
         kwargs={
             'section': 'flashtris',
             'category': 'screenshot',
             'template': 'screenshots.html',
         },
         name='flashtris_screenshots'),
    path('screenshots/<str:filename>/', images,
         kwargs={
             'section': 'flashtris',
             'category': 'screenshot',
             'template': 'screenshots.html',
         },
         name='flashtris_screenshot'),
    path('doc/',
         TemplateView.as_view(template_name='flashtris/doc.html'),
         name='flashtris_doc'),
    path('download/',
         TemplateView.as_view(template_name='flashtris/download.html'),
         name='flashtris_download'),
    path('dev/',
         TemplateView.as_view(template_name='flashtris/dev.html'),
         name='flashtris_dev'),
    path('faq/',
         TemplateView.as_view(template_name='flashtris/faq.html'),
         name='flashtris_faq'),
    path('support/',
         TemplateView.as_view(template_name='flashtris/support.html'),
         name='flashtris_support'),
]
