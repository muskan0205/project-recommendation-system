# Generated by Django 3.0.2 on 2020-11-21 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0010_auto_20201121_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendedrepossimilarity',
            name='similarity',
            field=models.CharField(default='-', max_length=10),
        ),
    ]
