from django.conf.urls.defaults import *
from list.models import ShoppingList

urlpatterns = patterns('list.views',
    url(r'^(\d+)/$', 'detail'),

)
