# Generated by Django 2.2.4 on 2019-08-25 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190825_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='core.Ingredients', verbose_name='Ingredientes'),
        ),
    ]
