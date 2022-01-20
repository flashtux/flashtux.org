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

"""Views for news."""

from datetime import datetime

from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import pytz

from flashtux.news.models import Info, Comment, CommentFormAdd


def paginate_news(request, info_list, pagesize):
    """Paginate list of news."""
    paginator = Paginator(info_list, pagesize)
    page = request.GET.get('page')
    try:
        infos = paginator.page(page)
    except PageNotAnInteger:
        infos = paginator.page(1)
    except EmptyPage:
        infos = paginator.page(paginator.num_pages)

    first_page = max(infos.number - 2, 1)
    last_page = min(infos.number + 2, paginator.num_pages)
    if first_page == 3:
        first_page = 1
    if last_page == paginator.num_pages - 2:
        last_page = paginator.num_pages
    smart_page_range = range(first_page, last_page + 1)

    return (infos, smart_page_range)


def render_news(request, section, info_list, **kwargs):
    """Render the paginated news."""
    pagesize = request.GET.get('pagesize', 10)
    try:
        pagesize = max(int(pagesize), 1)
    except ValueError:
        pagesize = 10
    infos, smart_page_range = paginate_news(request, info_list, pagesize)
    data = {
        'section': section,
        'infos': infos,
        'smart_page_range': smart_page_range,
        'pagesize': pagesize,
    }
    data.update(kwargs)
    return render(
        request,
        f'{section}/news.html',
        data,
    )


def get_comments_list(comments):
    """Return a list of comments with replies inside comments."""

    def get_comments(id_relative):
        """Recursively get comments for a relative id."""
        list_comments = []
        comments = comments_dict.get(id_relative, [])
        for comment in comments:
            comment.replies = get_comments(comment.id)
            list_comments.append(comment)
        return list_comments

    if not comments:
        return []

    # build a dict of comments:
    # - keys are the relative id (or 0)
    # - values are list of comments
    comments_dict = {}
    for comment in comments:
        id_relative = (comment.comment_relative.id
                       if comment.comment_relative else 0)
        comments_dict.setdefault(id_relative, []).append(comment)

    return get_comments(min(comments_dict.keys()))


def news_section(request, section=None, info_id=None, **kwargs):
    """News for a specific section."""
    section = section or 'home'
    if info_id:
        info = get_object_or_404(Info, pk=info_id)
        comments = info.comment_set.all().order_by('date')
        comments_list = get_comments_list(comments)
        data = {
            'section': section,
            'info_id': info_id,
            'info': info,
            'comments': comments_list,
        }
        data.update(kwargs)
        return render(
            request,
            f'{section}/news.html',
            data,
        )
    if section != 'home':
        info_list = Info.objects.filter(section=section).order_by('-date')
    else:
        info_list = Info.objects.order_by('-date')
    return render_news(request, section, info_list, **kwargs)


def form_comment(request, section=None, info_id=None,
                 comment_relative_id=None):
    """Reply to a news/comment."""
    section = section or 'home'
    info = get_object_or_404(Info, pk=info_id)
    comment = None
    comments_list = None
    if comment_relative_id != '0':
        comment = get_object_or_404(Comment, pk=comment_relative_id)
        comments_list = get_comments_list([comment])

    if request.method == 'POST':
        form = CommentFormAdd(request.POST)
        if form.is_valid():
            # add comment in database
            timezone = pytz.timezone(settings.TIME_ZONE)
            now = datetime.now(tz=timezone)
            comment_relative_id = comment.id if comment else None
            comment = Comment(
                comment_relative_id=comment_relative_id,
                info_id=info.id,
                date=now,
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
            )
            comment.save()
            kwargs = {
                'section': section,
                'info_id': info_id,
            }
            return HttpResponseRedirect(reverse('info', kwargs=kwargs))
    else:
        form = CommentFormAdd(ctx_info=info, ctx_comment_relative=comment)

    return render(
        request,
        f'{section}/news.html',
        {
            'section': section,
            'info_id': info_id,
            'info': info,
            'comments': comments_list,
            'form': form,
        },
    )
