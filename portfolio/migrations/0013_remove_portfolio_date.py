# Generated by Django 2.1.7 on 2019-04-05 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_auto_20190404_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='date',
        ),
    ]
