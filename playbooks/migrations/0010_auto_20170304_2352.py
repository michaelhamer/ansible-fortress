# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-03-04 21:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('playbooks', '0009_playbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='App_Playbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname_pk', models.IntegerField()),
                ('playbook_pk', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OfekApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='playbook',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='playbook',
            name='name',
        ),
        migrations.AddField(
            model_name='playbook',
            name='playbook_path',
            field=models.FilePathField(default='test.yml', match='*.yml', max_length=200, path=None),
        ),
        migrations.AlterField(
            model_name='playbook',
            name='duration',
            field=models.CharField(choices=[('hour', 'hour'), ('day', 'day'), ('week', 'week')], default='hour', max_length=4),
        ),
        migrations.AlterField(
            model_name='playbook',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
