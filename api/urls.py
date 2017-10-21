from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^category/$', category_list),
    url(r'^product/(?P<pk>[0-9]+)/$', product_list),
    url(r'^order/$', order),
    url(r'^item/$', item),
]