# Generated by Django 2.2.4 on 2019-08-25 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
    ]
