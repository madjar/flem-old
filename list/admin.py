from django.contrib import admin
from list.models import ShoppingList, ExtraIngredient, NotNeededIngredient
from planning.models import Meal

class ExtraIngredientInline(admin.TabularInline):
    model = ExtraIngredient
    extra = 1

class MealInline(admin.TabularInline):
    model = Meal
    extra = 0

class ShoppingListAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    inlines = (MealInline, ExtraIngredientInline)


admin.site.register(ShoppingList, ShoppingListAdmin)
admin.site.register(ExtraIngredient)
admin.site.register(NotNeededIngredient)
