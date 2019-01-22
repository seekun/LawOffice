from django.conf.urls import url, include
from django.contrib import admin
# from django.urls import path
from web import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from web.views import index


urlpatterns = [
                  url('admin/', admin.site.urls),
                  url(r'^web/', include('web.urls')),
                  url(r'^$', index, name='index'),
                  url(r'mdeditor/', include('mdeditor.urls')),
                  # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
                  url(r'mdeditor/', include('mdeditor.urls')),
                  url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
                  url(r'^upload/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
