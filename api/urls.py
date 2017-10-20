from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^category/$', category_list),
    url(r'^category/(?P<pk>[0-9]+)/$', category_detail),
    url(r'^product/$', product_list),
    url(r'^product/(?P<pk>[0-9]+)/$', product_detail),
    url(r'^order/$', order),
    url(r'^item/$', item),
]