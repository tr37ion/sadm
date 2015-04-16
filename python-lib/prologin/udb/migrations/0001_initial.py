# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def initial_data(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    g = Group(name="Organizer", pk=1)
    g.save()
    g.permissions = Permission.objects.filter(codename__in=['change_user'])

    g = Group(name="root", pk=2)
    g.save()
    g.permissions = Permission.objects.all()


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(db_index=True, unique=True, max_length=64)),
                ('firstname', models.CharField(max_length=64, verbose_name='First name')),
                ('lastname', models.CharField(max_length=64, verbose_name='Last name')),
                ('uid', models.IntegerField(db_index=True, unique=True, verbose_name='UID')),
                ('group', models.CharField(choices=[('user', 'Contestant'), ('orga', 'Organizer'), ('root', 'root')],
                                           max_length=20)),
                ('password', models.CharField(max_length=64, help_text='pwgen -cnB 8')),
                ('shell', models.CharField(default='/bin/bash', max_length=64)),
                ('ssh_key', models.CharField(max_length=4096, verbose_name='SSH public key', null=True, blank=True)),
            ],
            options={
                'ordering': ('group', 'login'),
            },
        ),
        migrations.RunPython(initial_data),
    ]
