from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<product_id>\d+)/$', views.product_add, name='product_add'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
]
