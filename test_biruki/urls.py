from django.conf.urls import patterns, url
from django.contrib import admin

from airports import views


admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^$', views.main, name='home'),
                       url(r'^country/(?P<c_id>\d+)/$', views.get_country),
                       url(r'^city/(?P<c_id>\d+)/$', views.get_city),
                       url(r'^airport/(?P<air_id>\d+)/$', views.get_airport),

                       #url(r'^admin/', include(admin.site.urls)),
)
