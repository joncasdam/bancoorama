# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_conta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='data da cria\xe7\xe3o', null=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True, verbose_name='data da atualiza\xe7\xe3o', null=True)),
                ('valor_currency', djmoney.models.fields.CurrencyField(default=b'BRL', max_length=3, editable=False, choices=[(b'BRL', b'Reais'), (b'USD', 'US Dollar')])),
                ('valor', djmoney.models.fields.MoneyField(default=Decimal('0.0'), verbose_name='Valor', max_digits=10, decimal_places=2, default_currency=b'BRL')),
                ('tipo', models.IntegerField(default=1, null=True, verbose_name='Tipo', blank=True, choices=[(1, b'Saque'), (2, 'Dep\xf3sito')])),
                ('saldo_currency', djmoney.models.fields.CurrencyField(default=b'BRL', max_length=3, editable=False, choices=[(b'BRL', b'Reais'), (b'USD', 'US Dollar')])),
                ('saldo', djmoney.models.fields.MoneyField(default=Decimal('0.0'), verbose_name='Saldo', max_digits=10, decimal_places=2, default_currency=b'BRL')),
                ('conta', models.ForeignKey(related_name='transacoes', verbose_name='Conta', to='contas.Conta')),
            ],
            options={
                'verbose_name': 'Transa\xe7\xe3o',
                'verbose_name_plural': 'Transa\xe7\xf5es',
            },
        ),
    ]
