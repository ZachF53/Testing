# Generated by Django 2.1.7 on 2019-04-05 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0028_auto_20190405_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Additional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('message', models.TextField(default='')),
                ('text', models.CharField(default='', max_length=120)),
                ('background', models.CharField(default='', max_length=120)),
            ],
            options={
                'verbose_name_plural': 'Additional Services',
            },
        ),
    ]