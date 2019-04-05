# Generated by Django 2.1.7 on 2019-04-05 05:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_auto_20190405_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.FileField(default=django.utils.timezone.now, upload_to='portfolio/static/img'),
            preserve_default=False,
        ),
    ]