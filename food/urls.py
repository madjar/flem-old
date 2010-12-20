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
    (r'^(?P<id>\d+)/$', recipe_detail),
    (r'^(?P<id>\d+)/edit/$', recipe_edit),
    (r'^(?P<id>\d+)/ingredientwizard/$', recipe_ingredient_wizard),

)
