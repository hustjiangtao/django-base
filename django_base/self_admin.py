# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

from django.contrib import admin
from django.urls import path

site_name = 'XX管理系统'
admin.site.site_header = f'{site_name}系统'
admin.site.site_title = f'{site_name}系统'
admin.site.index_title = site_name

url = path('admin/', admin.site.urls),