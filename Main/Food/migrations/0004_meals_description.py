# Generated by Django 3.0.2 on 2020-02-03 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0003_meals_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='description',
            field=models.TextField(blank=True, max_length=750),
        ),
    ]