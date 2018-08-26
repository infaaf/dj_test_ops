#!/usr/bin/env python
# -*- coding=utf-8 -*-
# __author__ = 'infaaf'

from __future__ import absolute_import, unicode_literals
from celery import shared_task,subtask,task
from .utils.simple_allinone_ansible_runner import  Runner

@shared_task
def add(x, y):
    return x + y


###  debuging...
@shared_task
def example4():
    #  use adhoc  + dynamic inventory
    resource = {
        'group1': {'hosts': [{'hostid': '123', 'hostname': 'h1', 'hostip': '192.168.188.200', 'username': 'root',
                              'password': 'admin', 'port': '22', 'sshkey': '', 'k1': 'v1'},
                             {'hostid': '223', 'hostname': 'h2', 'hostip': '192.168.188.201', 'username': 'root',
                              'password': '1qaz@WSX', 'port': '22', 'sshkey': '', },
                             ],
                   'groupvars': {"g1key": "g1value"}},
        }
    runner = Runner(resource)
    print(runner.options)
    print("affter resource")
    runner.run_model(host_list=['h1'], module_name='shell', module_args='echo 1 >> /tmp/log2')

    result = runner.results_raw
    print('%s:%s'%(__name__,result))
    return result

