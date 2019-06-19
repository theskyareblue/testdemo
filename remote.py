#coding=utf-8
from fabric.api import *


env.hosts=['192.168.126.100', '192.168.126.200']
#env.password='python'
env.passwords = {
    'root@192.168.126.100:22':'123456',
    'root@192.168.126.200:22':'123456',
}

#@runs_once
def input_raw():
    return prompt("please input ip:", default="192.168.126.100")
def input_port():
    return prompt("please input port:", default="22")

def workask(ip, port):
    #run('ls /home')
    run('telnet ' + ip +'  ' + port)

@task
def go():
    print('start ...')
    getip = input_raw()
    getport = input_port()
    workask(getip, getport)
    print('end ...')
