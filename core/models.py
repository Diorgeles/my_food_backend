from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Recipe(SoftDeletableModel, TimeStampedModel):
    """Model definition for Students."""

    # TODO: Define fields here
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.CharField(max_length=8, editable=False)
    name = models.CharField('Nome', max_length=100)

    class Meta:
        """Meta definition for Students."""

        verbose_name = 'Estudante'
        verbose_name_plural = 'Estudantes'

    def __str__(self):
        """Unicode representation of Students."""
        return self.name

