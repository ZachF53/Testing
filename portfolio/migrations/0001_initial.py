# Generated by Django 2.1.7 on 2019-04-05 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('site', models.CharField(max_length=250)),
                ('rate', models.FloatField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
