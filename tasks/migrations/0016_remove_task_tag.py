# Generated by Django 2.1.7 on 2019-03-05 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_auto_20190305_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='tag',
        ),
    ]
