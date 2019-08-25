from rest_framework import serializers
from .models import Ingredients, Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('__all__')
        depth = 1


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('__all__')
        depth = 1
