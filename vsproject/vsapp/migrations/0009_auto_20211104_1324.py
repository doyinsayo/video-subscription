# Generated by Django 3.0.2 on 2021-11-04 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vsapp', '0008_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='directors',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='writers',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
