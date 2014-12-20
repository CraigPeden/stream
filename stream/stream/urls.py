from django.conf.urls import patterns, include, url
from django.contrib import admin
from web import views

urlpatterns = patterns('',

	# Admin

    url(r'^admin/', include(admin.site.urls)),
    
    # Authentication
    
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^register/$', views.registerView.as_view()),
    
    # App
    
    url(r'^$', views.index.as_view()),
    url(r'^(?P<broadcaster_username>\w+)/$', views.stream.as_view()),
)
