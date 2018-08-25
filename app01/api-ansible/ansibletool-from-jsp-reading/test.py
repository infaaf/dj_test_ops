from app01.lib.ansibletool.runner import  PlayBookRunner


if __name__ == '__main__':

    playbook=PlayBookRunner('/etc/ansible/hosts','/etc/ansible/myplay.yaml')
    playbook.run()