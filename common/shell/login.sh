#!/bin/bash

filename=$1


cat ${filename} | while read line
do
	host_ip=`echo $line | awk '{print $1}'`
	host_pwd=`echo $line | awk '{print $2}'`      
	host_port=`echo $line | awk '{print $3}'`
	./login.exp ${username} ${host_port} ${host_ip} ${host_pwd}
done
