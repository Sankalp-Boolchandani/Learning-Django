# Generated by Django 5.1.4 on 2025-03-13 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0008_student_is_delete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='is_delete',
            new_name='is_deleted',
        ),
    ]
