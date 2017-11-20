from django.conf.urls import url
from . import views

app_name = 'webapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create_product, name='create_product'),
    url(r'^get/$', views.get_product, name='get_product'),
    url(r'^delete/(?P<id>[0-9]+)/$', views.delete_product, name='delete_product'),
    url(r'^modify/(?P<id>[0-9]+)/$', views.modify_product, name='modify_product'),
]