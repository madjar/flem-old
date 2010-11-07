from django.contrib import admin
from list.models import ShoppingList, ExtraIngredient, NotNeededIngredient

class ExtraIngredientInline(admin.TabularInline):
    model = ExtraIngredient
    extra = 1

class ShoppingListAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    inlines = (ExtraIngredientInline,)


admin.site.register(ShoppingList, ShoppingListAdmin)
admin.site.register(ExtraIngredient)
admin.site.register(NotNeededIngredient)
