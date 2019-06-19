file=$1


###文件传输
/usr/bin/ansible mh_api_4 -m copy -a "src=/data/upload/version/mh/${file} dest=/hnisi/webapp/"

if [ $? -eq 2 ];then
	echo "压缩包不存在"
	exit 0
fi

/usr/bin/ansible mh_api_4 -m shell -a "chown hnisi:hnisi /hnisi/webapp/${file} warn=False"

/usr/bin/ansible mh_api_4 -m shell -a "ls -l /hnisi/webapp/${file}"


###停止8089应用
###/usr/bin/ansible mh_api_4 -m shell -a "su - hnisi -c '/hnisi/middleware/8089/bin/shutdown.sh' warn=False"
###sleep 3s
###/usr/bin/ansible mh_api_4 -m shell -a "ps -ef|grep tomcat |grep 8089|grep -v grep"
###if [ $? -eq 0 ];then
###/usr/bin/ansible mh_api_4 -m shell -a "ps -ef|grep tomcat |grep 8089|grep -v grep| awk '{print \$2}' | xargs kill -9"
###fi

/usr/bin/ansible mh_api_4 -m shell -a "ps -ef|grep tomcat |grep 8089|grep -v grep| awk '{print \$2}' | xargs kill -9"


###备份应用和静态文件
/usr/bin/ansible mh_api_4 -m shell -a "cp -r /hnisi/webapp/gdsx_newportal /hnisi/webapp/backup/gdsx_newportal_`date +%Y%m%d`" 
/usr/bin/ansible mh_api_4 -m shell -a "cp -r /hnisi/webapp/static /hnisi/webapp/backup/static_`date +%Y%m%d`" 


###解压压缩包拷贝static
/usr/bin/ansible mh_api_4 -m shell -a "su - hnisi -c 'unzip -o /hnisi/webapp/${file} -d /hnisi/webapp/' warn=False"

/usr/bin/ansible mh_api_4 -m shell -a "su - hnisi -c '\cp -r /hnisi/webapp/gdsx_newportal/static /hnisi/webapp/'"


###启动8089应用
/usr/bin/ansible mh_api_4 -m shell -a "su - hnisi -c '/hnisi/middleware/8089/bin/startup.sh' warn=False"
/usr/bin/ansible mh_api_4 -m shell -a "ps -ef|grep tomcat |grep 8089|grep -v grep"




sed 's/.*/\/hnisi\/webapp\/gdsx_newportal\/&/' /hnisi/webapp/gdsx_newportal/deleteInfo.log
sed -i "{s/^/'/g;s/$/'/g}" deleteInfo.log




/usr/bin/ansible mh_out_api -m copy -a "src=/data/upload/version/mh/Outapi_1.0.0__20180825_142299.zip dest=/hnisi/webapp/"
