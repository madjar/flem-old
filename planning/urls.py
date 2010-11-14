from django.conf.urls.defaults import *

urlpatterns = patterns('planning.views',
    url(r'^(?P<year_from>\d{4})/(?P<month_from>\d{2})/(?P<day_from>\d+)/'
        r'(?P<year_to>\d{4})/(?P<month_to>\d{2})/(?P<day_to>\d+)/$', 'range'),

)
