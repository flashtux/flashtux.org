# SPDX-FileCopyrightText: 1999-2026 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

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
