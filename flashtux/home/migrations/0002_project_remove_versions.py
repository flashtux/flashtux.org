# Generated by Django 2.2.28 on 2023-04-16 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='devel_version',
        ),
        migrations.RemoveField(
            model_name='project',
            name='stable_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='stable_version',
        ),
    ]