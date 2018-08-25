from django.shortcuts import render,HttpResponse
from app01.lib.test2 import  AnsibleAPI

# Create your views here.
import logging
logger=logging.getLogger(__name__)

def index(request):
    print(__name__)
    logger.error('eeee')

    an1 = AnsibleAPI('192.168.188.200,192.168.188.200', 'test1.py', ['/etc/ansible/myplay.yaml'])
    an1.runplaybook()
    # an2 = AnsibleAPI('192.168.194.128','common-oss-dc3a25.tar',['/etc/ansible/myplay.yaml'])
    # processes = []
    # p1 = multiprocessing.Process(name='process_one', target=an1.runplaybook)
    # # p2 = multiprocessing.Process(name='process_two',target=an1.runplaybook)
    # # processes.append(p1)
    # # processes.append(p2)
    # # for p in processes:
    # #	p.start()
    #
    # # 等待子进程结束，主进程退出
    # # for p in processes:
    # #	p.join()	#可以加浮点数参数，等待多久就不等了
    # p1.start()
    # if p1.is_alive():
    #     print('正在发布')
    # p1.join()
    # if not p1.is_alive():
    #     print('发布结束')





    return HttpResponse('index:::%s'%(__name__))