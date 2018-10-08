ansible 与 celery 调试通过。

#ansible2.4+ api 
# celery 异步

install redis
yum install -y http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
yum --enablerepo=remi install redis
service  redis start
chkconfig redis on
pip3 install celery
pip3 install celery[redis]
