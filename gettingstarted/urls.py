from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    #url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myverb/', hello.views.myverb, name='myverb'),
    url(r'^echo/', hello.views.echo, name='echo'),
    url(r'^$', hello.views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', hello.views.post_detail, name='post_detail'),
]
