# -*- encoding: utf-8 -*-
from django.db import models

from base.models import Banco


class Agencia(models.Model):
    banco = models.ForeignKey(Banco, verbose_name=u'Banco', related_name='agencias')
    codigo = models.IntegerField(u'Código', editable=False, unique=True)

    class Meta:
        verbose_name = u'Agência'
        verbose_name_plural = u'Agências'

