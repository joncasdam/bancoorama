# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_banco'),
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='data da cria\xe7\xe3o', null=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True, verbose_name='data da atualiza\xe7\xe3o', null=True)),
                ('numero', models.IntegerField(verbose_name='N\xfamero', unique=True, editable=False)),
                ('saldo_currency', djmoney.models.fields.CurrencyField(default=b'BRL', max_length=3, editable=False, choices=[(b'BRL', b'Reais'), (b'USD', 'US Dollar')])),
                ('saldo', djmoney.models.fields.MoneyField(default=Decimal('0.0'), max_digits=10, decimal_places=2, default_currency=b'BRL')),
                ('agencia', models.ForeignKey(related_name='contas', verbose_name='Ag\xeancia', to='contas.Agencia')),
                ('correntista', models.ForeignKey(related_name='conta', verbose_name='Correntista', to='base.Perfil')),
            ],
            options={
                'verbose_name': 'Conta',
                'verbose_name_plural': 'Contas',
            },
        ),
    ]
