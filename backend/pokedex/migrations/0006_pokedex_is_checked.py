# Generated by Django 2.2.7 on 2019-12-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0005_remove_pokedex_is_checked'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokedex',
            name='is_checked',
            field=models.BooleanField(default=False),
        ),
    ]
