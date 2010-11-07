from food.models import Section, Category, Ingredient, Recipe, Containment
from django.contrib import admin

class ContainmentInline(admin.TabularInline):
    model = Containment
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = (ContainmentInline,)

admin.site.register(Section)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
