# Generated by Django 3.0.2 on 2021-05-22 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vsapp', '0004_auto_20210522_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='detail_text',
            field=models.TextField(max_length=200, verbose_name='Detail Text'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='preview_text',
            field=models.TextField(max_length=100, verbose_name='Preview Text'),
        ),
    ]
