from django.shortcuts import render,HttpResponse
from .utils.simple_allinone_ansible_runner import Runner as AnsibleRunner
from .tasks import add

# Create your views here.
import logging
logger=logging.getLogger(__name__)

def index(request):
    r=add.delay(3,4)
    # print(r.ready())
    import time
    time.sleep(1)
    print(r.get(timeout=3))
    return HttpResponse('123')
