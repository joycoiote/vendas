# coding: utf-8
from django.conf.urls import patterns, include, url
from vendas.views import *
from vendas.models import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index.as_view(), name='home'),
    url(r'^client/$', ClientList.as_view(), name='client_list'),
    url(r'^category/$', CategoryList.as_view(), name='category_list'),
    url(r'^product/$', ProductList.as_view(), name='product_list'),
    url(r'^sale/$', SaleList.as_view(), name='sale_list'),
    url(r'^sale/(?P<pk>\d+)/$', SaleDetailView.as_view(), name='sale_detail'),
    url(r'^about/$', About.as_view(), name='about'),
)
