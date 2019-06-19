#!/bin/bash

#file=$1

#/usr/bin/ansible a -m copy -a "src=${file} dest=/hnisi/webapp/"
#/usr/bin/ansible a -m shell -a "chown oracle:oinstall /hnisi/webapp/${file} warn=False"

#/usr/bin/ansible a -m shell -a "su - oracle -c 'unzip -o /hnisi/webapp/${file} -d /hnisi/webapp/' warn=False"

#/usr/bin/ansible a -m shell -a "su - oracle -c '\cp -r /hnisi/webapp/gdsx_newportal/static /hnisi/webapp/'"



/usr/bin/ansible a -m shell -a "ps -ef |grep tomcat |grep -v grep"

sleep 1s



/usr/bin/ansible a -m shell -a "ls /hnisi/webapp/gdsx_newportal/deleteInfo.log"
if [ $? -eq 0 ];then
/usr/bin/ansible a -m shell -a "/usr/bin/dos2unix /hnisi/webapp/gdsx_newportal/deleteInfo.log"
/usr/bin/ansible a -m shell -a "sed -i 's/.*/\/hnisi\/webapp\/gdsx_newportal\/&/' /hnisi/webapp/gdsx_newportal/deleteInfo.log warn=False"
#/usr/bin/ansible a -m shell -a "sed -i "{s/^/'/g;s/$/'/g}" /hnisi/webapp/gdsx_newportal/deleteInfo.log"
#/usr/bin/ansible a -m shell -a "sed -i ""s/^/'/g"" /hnisi/webapp/gdsx_newportal/deleteInfo.log"
#/usr/bin/ansible a -m shell -a "sed -i ""s/$/'/g"" /hnisi/webapp/gdsx_newportal/deleteInfo.log"
/usr/bin/ansible a -m shell -a "/hnisi/webapp/gdsx_newportal/sed.sh"

/usr/bin/ansible a -m shell -a "su - oracle -c '/opt/local/apache-tomcat-8.0.52/bin/startup.sh' warn=False"
else
	echo "没有此文件"
	/usr/bin/ansible a -m shell -a "su - oracle -c '/opt/local/apache-tomcat-8.0.52/bin/startup.sh' warn=False"
fi

echo "12143325435265"
1214e325r4365t435325r
q354rqafagadgf
