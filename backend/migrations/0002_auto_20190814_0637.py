# Generated by Django 2.2.4 on 2019-08-14 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='active_plan',
            field=models.CharField(default='No active plan', max_length=100),
        ),
    ]
