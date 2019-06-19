#!/bin/bash
#

server_list=$1

polysh --hosts-file="$server_list" --password-file="host_pwd"  --ssh='ssh -l root -p22 '
