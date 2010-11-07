from django.contrib import admin
from list.models import ShoppingList, ExtraIngredient, NotNeededIngredient

admin.site.register(ShoppingList)
admin.site.register(ExtraIngredient)
admin.site.register(NotNeededIngredient)
