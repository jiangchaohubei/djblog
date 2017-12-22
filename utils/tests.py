#!/usr/bin/env python
# -*- coding:utf8 -*-
from django.test import TestCase
from utils.paginator import getPages

class paginatorTest(TestCase):

    def setUp(self):
        pass

    def test_getPages(self):
        paginator,objectList=getPages(16,[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
        print paginator.page_range_ex

    def tearDown(self):
        pass