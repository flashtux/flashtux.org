#
# Copyright (C) 1999-2020 Sébastien Helleu <flashcode@flashtux.org>
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

"""Views for image."""

from django.shortcuts import render, get_object_or_404

from flashtux.image.models import Image


def images(request, section, category, template, filename=''):
    """
    Page with one image (if filename given),
    or all images as thumbnails.
    """
    if filename:
        image = get_object_or_404(Image, section=section, category=category,
                                  filename=filename)
        return render(
            request,
            f'{section}/{template}',
            {
                'section': section,
                'category': category,
                'filename': filename,
                'image': image,
            },
        )

    image_list = (Image.objects
                  .filter(section=section)
                  .filter(category=category)
                  .order_by('priority'))
    return render(
        request,
        f'{section}/{template}',
        {
            'section': section,
            'category': category,
            'image_list': image_list,
        },
    )
