# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_transacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='correntista',
            field=models.OneToOneField(related_name='conta', verbose_name='Correntista', to='base.Perfil'),
        ),
    ]
