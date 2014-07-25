from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from api import views

router = routers.DefaultRouter()

router.register(r'messages', views.MessageViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sdbparserapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
