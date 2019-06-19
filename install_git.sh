#!/bin/bash


function install_git(){

git_tgz=`find / -name "git-2.9.5.tar.gz"`

if [ ! -d /data/common/local ];then
	mkdir -p /data/common/local
fi


tar -xf ${git_tgz} -C /tmp/

cd /tmp/git-2.9.5

./configure --prefix=/data/common/local/git_2.9.5

make && make install

ln -s /data/common/local/git_2.9.5/bin/* /usr/bin/


}

install_git
