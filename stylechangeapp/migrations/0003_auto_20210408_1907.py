# Generated by Django 3.0 on 2021-04-08 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stylechangeapp', '0002_auto_20210408_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='styleimage',
            name='style_image',
            field=models.ImageField(upload_to='documents/'),
        ),
    ]