# Generated by Django 2.2.1 on 2019-05-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0005_archive_displayname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='displayname',
            field=models.CharField(max_length=200),
        ),
    ]
