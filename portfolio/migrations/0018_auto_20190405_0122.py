# Generated by Django 2.1.7 on 2019-04-05 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_auto_20190405_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.FileField(upload_to='portfolio/static/img/port'),
        ),
    ]