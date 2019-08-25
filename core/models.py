from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Recipe(SoftDeletableModel, TimeStampedModel):
    """Model definition for Students."""

    # TODO: Define fields here
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Nome', max_length=100, null=True, blank=True)
    description = models.TextField('Descrição', max_length=255, null=True, blank=True)
    ingredients = models.ManyToManyField('Ingredientes', max_length=8, editable=False)

    class Meta:
        """Meta definition for Students."""

        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'

    def __str__(self):
        """Unicode representation of Students."""
        return self.name

class Ingredients(SoftDeletableModel, TimeStampedModel):

    MEASURE_TYPE = [
        ('spoon', 'Colher'),
        ('cup', 'Xícara'),
    ]

    name = models.CharField('Nome', max_length=100, null=True, blank=True)
    amount = models.IntegerField('Quatidade', max_length=100, null=True, blank=True)
    measure = models.CharField('Medida', max_length=100, null=True, blank=True, choices=MEASURE_TYPE)

    class Meta:
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'

    def __str__(self):
        """Unicode representation of Students."""
        return self.name


