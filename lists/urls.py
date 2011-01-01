from django.conf.urls.defaults import *

urlpatterns = patterns('lists.views',
    url(r'^(\d+)/$', 'detail'),

)
