# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_banco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.IntegerField(verbose_name='C\xf3digo', unique=True, editable=False)),
                ('banco', models.ForeignKey(related_name='agencias', verbose_name='Banco', to='base.Banco')),
            ],
            options={
                'verbose_name': 'Ag\xeancia',
                'verbose_name_plural': 'Ag\xeancias',
            },
        ),
    ]
