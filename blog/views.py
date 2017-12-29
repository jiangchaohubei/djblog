#!/usr/bin/env python
# -*- coding:utf8 -*-
from django.shortcuts import render_to_response
from blog.models import Blog
from utils.paginator import getPages
import traceback
# Create your views here.


def blog_select(request):
    try:
        data={}
        #获取GET请求的参数，得到当前页码。若没有该参数，默认为1
        current_page = request.GET.get("page", 1)
        blogs=Blog.objects.all()
        pages,blogsList=getPages(current_page,blogs)

        data["pages"]=pages
        data["blogs"]=blogsList
    except Exception,e:
        traceback.print_exc()

    return render_to_response('templates/blog/blog_list.html',data)

