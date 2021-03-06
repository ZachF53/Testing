# Generated by Django 2.1.7 on 2019-04-05 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_auto_20190405_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='height_field',
            field=models.IntegerField(default=200),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='width_field',
            field=models.IntegerField(default=200),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='portfolio/static/img', width_field='width_field'),
        ),
    ]
