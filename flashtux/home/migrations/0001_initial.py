# Generated by Django 2.2.28 on 2023-04-16 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('start_date', models.DateField()),
                ('stable_version', models.CharField(blank=True, max_length=32)),
                ('stable_date', models.DateField(blank=True, null=True)),
                ('devel_version', models.CharField(blank=True, max_length=32)),
                ('description', models.TextField()),
                ('license', models.CharField(max_length=32)),
                ('support', models.CharField(blank=True, max_length=1024)),
                ('page', models.CharField(max_length=1024)),
                ('website', models.CharField(blank=True, max_length=1024)),
                ('repository', models.CharField(blank=True, max_length=1024)),
                ('screenshot', models.CharField(blank=True, max_length=1024)),
                ('priority', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['priority'],
            },
        ),
    ]
