from django.contrib import admin
from lists.models import ShoppingList, ExtraIngredient, NotNeededIngredient
from planning.models import Meal

class MealInline(admin.TabularInline):
    model = Meal
    extra = 0

class ExtraIngredientInline(admin.TabularInline):
    model = ExtraIngredient
    extra = 1

class NotNeededIngredientInline(admin.TabularInline):
    model = NotNeededIngredient
    extra = 1

class ShoppingListAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    inlines = (MealInline, ExtraIngredientInline, NotNeededIngredientInline)


admin.site.register(ShoppingList, ShoppingListAdmin)
