# Generated by Django 4.2.2 on 2023-09-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='products',
            field=models.ManyToManyField(default=False, to='api.product'),
        ),
    ]