from django.conf.urls import url
from .views import IndexPage, LessonPage

urlpatterns = [
    url(r'^$', IndexPage.as_view(), name='index_page'),
    url(r'^lesson/(?P<book>\w+)/(?P<template>\w+)/$', LessonPage.as_view(), name='lesson'),

]