#!/bin/bash


#filename=$1

#rm -rf ./host_ip
#rm -rf ./host_pwd

#cat ${filename} | while read host_ip host_pwd host_port
#do
#echo "${host_ip}" >> ./host_ip
#echo "${host_pwd}" > ./host_pwd
#done

polysh --hosts-file="./host_ip" --password-file="./host_pwd" --ssh='ssh -l root -p22 '
