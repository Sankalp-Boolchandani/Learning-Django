# Generated by Django 5.1.4 on 2025-03-11 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0006_alter_subjectmarks_student_delete_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('date_of_rank_generation', models.DateField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentrank', to='college.student')),
            ],
            options={
                'unique_together': {('student', 'date_of_rank_generation')},
            },
        ),
    ]
