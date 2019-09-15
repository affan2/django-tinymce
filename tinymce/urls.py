# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)
from django.conf.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^spellchecker/$', views.spell_check, name='tinymce-spellcheck'),
    re_path(r'^flatpages_link_list/$', views.flatpages_link_list, name='tinymce-linklist'),
    re_path(r'^compressor/$', views.compressor, name='tinymce-compressor'),
    re_path(r'^filebrowser/$', views.filebrowser, name='tinymce-filebrowser'),
]
