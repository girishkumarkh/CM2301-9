from django.conf.urls import patterns, include, url

uuid = '[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'

urlpatterns = patterns('',
    # /
    url(r'^$', 'learn.views.home', name='home'),
    #url(r'^videos/$', 'learn.views.videos'),
    url(r'^videos/submit/$', 'learn.views.video_submit'),
    url(r'^login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
    
    #Video URL's
    url(r'^videos/$', 'learn.views.videos'),
    url(r'^videos/(?P<video_id>%s)/$' % (uuid), 'learn.views.video'),
    url(r'^videos/(?P<video_id>%s)/serve/(.+)$' % (uuid), 'learn.views.serve_video'),
    url(r'^videos/create/$', 'learn.views.video_create'),
    
    #Lecture URL's
    url(r'^lectures/create/$', 'learn.views.lecture_create'),
)
