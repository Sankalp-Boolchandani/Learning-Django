# Generated by Django 5.1.4 on 2025-03-12 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0010_alter_recipe_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
