from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path

app_name = 'web'

urlpatterns = (
    url(r'^index/', views.index, name='index'),
    url(r'^services/', views.services, name='services'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^test1/', views.test1, name='test1'),
    url(r'^detail/(?P<id>.*?)$', views.detail, name='detail'),
    url(r'^about/', views.about, name='about'),
    url(r'^news/', views.news, name='news'),
    url(r'^news_detail/(?P<id>.*?)$', views.news_detail, name='news_detail'),

)