#!/usr/bin/env python
# -*- coding=utf-8 -*-
# __author__ = 'infaaf'

from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def add(x, y):
    return x + y