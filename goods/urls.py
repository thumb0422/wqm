# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import path
from goods import views

# urlpatterns = [
#     url(r'^$', index, name='index'),
# ]


urlpatterns = [
    path('goods/', views.goods_list),
    path('goods/<int:pk>/', views.goods_detail),
]