from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path


app_name = 'web'

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^services/', views.services, name='services'),
    url(r'^test1/', views.test1, name='test1'),
    url(r'^detail/(?P<id>.*?)$', views.detail, name='detail'),

]