#!/usr/bin/env python
# -*- coding:utf8 -*-

from django.core.paginator import Paginator
from django.conf import settings


def getPages(currentPage=1,objectList=[]):
    '''get the paginator'''

    paginator=Paginator(objectList,settings.EACHPAGE_NUMBER)
    objectList=paginator.page(currentPage)

    page_range = []
    current = objectList.number     #当前页码
    page_all = paginator.num_pages  #总页数
    mid_pages = 3                   #中间段显示的页码数
    page_goto = 1                   #默认跳转的页码

    if page_all <= 2 + mid_pages:
        #页码数少于6页就无需分析哪些地方需要隐藏
        page_range = paginator.page_range
    else:
        #添加应该显示的页码
        page_range += [1, page_all]
        page_range += [current-1, current, current+1]

        #若当前页是头尾，范围拓展多1页
        if current == 1 or current == page_all:
            page_range += [current+2, current-2]

        #去掉超出范围的页码
        #filter过滤函数，lambda匿名函数表达式
        page_range = filter(lambda x: x>=1 and x<=page_all, page_range)

        #排序去重
        #set去重无序元素集，sorted排序产生新的有序列表
        page_range = sorted(list(set(page_range)))

        step1 = page_range[1]-page_range[0]
        if step1 == 2:
            page_range.insert(1,2)
        elif step1 > 2:
            page_range.insert(1,'...')

        step2 = page_range[len(page_range)-1]-page_range[len(page_range)-2]
        if step2 == 2:
            page_range.insert(len(page_range)-1,page_all-1)
        elif step2 > 2:
            page_range.insert(len(page_range)-1,'...')


    #优化结果之后的页码列表
    paginator.page_range_ex = page_range
    #默认跳转页的值
    paginator.page_goto = page_goto

    return paginator,objectList