# Generated by Django 2.2.1 on 2019-05-16 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0002_auto_20190516_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='displayname',
            field=models.CharField(default=models.CharField(max_length=200), max_length=200),
        ),
    ]
