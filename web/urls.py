from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path


app_name = 'web'
urlpatterns = [
    # url(r'^index/', views.index, name='index'),
    url(r'^index/', views.index, name='index'),

    url(r'^about/', views.about, name='about'),
    url(r'^news/', views.news, name='news'),
    url(r'^news_detail/(?P<id>.*?)$', views.news_detail, name='news_detail'),
    url(r'^services/', views.services, name='services'),

]