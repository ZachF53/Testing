# Generated by Django 2.1.7 on 2019-04-05 01:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_remove_portfolio_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
    ]