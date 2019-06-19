#!/usr/bin/env python
# encoding: utf-8


import argparse
parser = argparse.ArgumentParser(description='this is hello')
parser.add_argument('-s',help='this is a number',dest='abc')
parse = parser.parse_args()

print parse.abc


#action_dict = {"backup":backup,"wget_unzip":wget_unzip,"backup_update":backup_update,"start_process":start_process,"stop_process":stop_process,"rollback":rollback,"check_file_md5":check_file_md5,"check_process":check_process,"check_process_port":check_process_port,"change_mod":change_mod,}

def backup():
	pass

def tom():
	pass

asd = {"backupu1":backup,"name1":tom}
print asd.keys()
