from rest_framework import viewsets
from .serializers import IngredientsSerializer, RecipeSerializer
from .models import Ingredients, Recipe


class IngredientsViewSet(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
