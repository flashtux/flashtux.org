# Generated by Django 2.2.28 on 2023-04-16 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1024)),
                ('content', models.TextField()),
                ('priority', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['priority'],
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'rejected'), (1, 'waiting for approval'), (2, 'blacklisted'), (3, 'fixed')])),
                ('lang', models.CharField(max_length=32)),
                ('website', models.CharField(max_length=256)),
                ('url', models.CharField(max_length=256)),
                ('contact', models.CharField(blank=True, max_length=256)),
                ('shortdesc', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True)),
                ('internet_explorer', models.CharField(blank=True, max_length=1)),
                ('konqueror', models.CharField(blank=True, max_length=1)),
                ('chrome', models.CharField(blank=True, max_length=1)),
                ('mozilla', models.CharField(blank=True, max_length=1)),
                ('opera', models.CharField(blank=True, max_length=1)),
                ('win', models.CharField(blank=True, max_length=1)),
                ('mac', models.CharField(blank=True, max_length=1)),
                ('unix', models.CharField(blank=True, max_length=1)),
                ('severity', models.IntegerField(choices=[(1, 'display issues'), (2, 'partially broken'), (3, 'entirely broken')])),
                ('sentmail', models.TextField(blank=True)),
                ('recvmail', models.TextField(blank=True)),
                ('date', models.DateField()),
                ('date_update', models.DateField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=256)),
                ('email', models.CharField(blank=True, max_length=256)),
            ],
            options={
                'ordering': ['-date', 'website'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=256)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='w3blacklist.Site')),
            ],
        ),
    ]