from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^images/(?P<path>.*)/$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    url(r'^(?P<project_id>[0-9]+)/$', views.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
