# Generated by Django 2.1.7 on 2019-02-16 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='date_of_ending',
            field=models.DateTimeField(null=True),
        ),
    ]
