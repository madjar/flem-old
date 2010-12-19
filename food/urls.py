from django.conf.urls.defaults import *
from django.views.generic import list_detail
from food.models import Recipe
from food.views import *


recipe_info = {
    "queryset"              : Recipe.objects.all(),
    'template_object_name'  : "recipe",
}

urlpatterns = patterns('',
    (r'^$', list_detail.object_list, recipe_info),
    url(r'^(?P<object_id>\d+)/$', list_detail.object_detail, recipe_info, name='recipe_view'),
    (r'^(?P<id>\d+)/edit/$', recipe_edit)

)
