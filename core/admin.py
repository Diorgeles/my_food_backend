from django.contrib import admin
from .models import Recipe, Ingredients


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'description']
    filter_horizontal = ('ingredients',)



@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'measure']
