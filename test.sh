#!/bin/bash

file=$1

/usr/bin/ansible a -m copy -a "src=${file} dest=/opt/"
#echo $?

#/usr/bin/ansible a -m copy -a "src=aaa dest=/opt/"
if [ $? -eq 2 ];then
	echo "文件不存在"
	exit 0
fi
/usr/bin/ansible a -m shell -a "su - oracle -c '/opt/local/apache-tomcat-8.0.52/bin/startup.sh' warn=False"
echo $?
/usr/bin/ansible a -m shell -a "ps -ef |grep tomcat |grep -v grep"
echo $?

/usr/bin/ansible a -m shell -a "ps -ef |grep tomcat1 |grep -v grep"
echo $?


#sleep 10s

#/usr/bin/ansible a -m shell -a "su - oracle -c '/opt/local/apache-tomcat-8.0.52/bin/shutdown.sh' warn=False"
#echo $?
