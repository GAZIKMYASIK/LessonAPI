# Generated by Django 4.2.2 on 2023-09-24 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_lesson_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlesson',
            name='status',
        ),
    ]