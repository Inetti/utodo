# Generated by Django 2.1.7 on 2019-03-05 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0019_auto_20190305_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Tag'),
        ),
    ]