# Generated by Django 2.1.7 on 2019-04-05 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0025_auto_20190405_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='color',
            field=models.CharField(default='', max_length=120),
        ),
    ]
