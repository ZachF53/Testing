# Generated by Django 2.1.7 on 2019-04-05 21:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0023_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='option1',
        ),
        migrations.RemoveField(
            model_name='services',
            name='option2',
        ),
        migrations.RemoveField(
            model_name='services',
            name='option3',
        ),
        migrations.AddField(
            model_name='services',
            name='mesage',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]