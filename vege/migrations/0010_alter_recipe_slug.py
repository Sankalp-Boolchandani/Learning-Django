# Generated by Django 5.1.4 on 2025-03-12 20:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0009_alter_recipe_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2025, 3, 12, 20, 40, 43, 753441, tzinfo=datetime.timezone.utc), unique=True),
        ),
    ]
