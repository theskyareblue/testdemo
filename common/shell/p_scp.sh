#!/bin/bash 
                
  src_file=$1
  username=$2
  host_list=$3
  dest_file=$4
  #password=$5
  cat $host_list | while read line 
  do
      host_ip=`echo $line | awk '{print $1}'` 
      host_pwd=`echo $line | awk '{print $2}'`
      ./s_scp.exp $src_file $username $host_ip $dest_file ${host_pwd}
  done
#./p_scp.sh aa root dest_ip /root/common/shell/bb
