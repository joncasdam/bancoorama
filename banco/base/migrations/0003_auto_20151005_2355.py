# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_banco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='tipo',
            field=models.IntegerField(default=1, null=True, verbose_name='Tipo', blank=True, choices=[(1, 'Correntista'), (2, 'Administrador')]),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(related_name='perfil', verbose_name='Usu\xe1rio', to=settings.AUTH_USER_MODEL),
        ),
    ]
