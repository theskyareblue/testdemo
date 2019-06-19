#!/bin/bash

<<!
i=`date +"%m"`
if [ "${i}"x == "01"x ];then
	j="Jan"
elif [ "${i}"x == "02"x ];then
        j="Feb"
elif [ "${i}"x  == "03"x ];then
        j="Mar"
elif [ "${i}"x  == "04"x ];then
        j="Apr"
elif [ "${i}"x  == "05"x ];then
        j="May"
elif [ "${i}"x  == "06"x ];then
        j="Jun"
elif [ "${i}"x  == "07"x ];then
        j="Jul"
elif [ "${i}"x  == "08"x ];then
        j="Aug"
elif [ "${i}"x  == "09"x ];then
        j="Sep"
elif [ "${i}"x  == "10"x ];then
        j="Oct"
elif [ "${i}"x  == "11"x ];then
        j="Nov"
else 
	j="Dec"
fi
echo "${j}"
!

store_day=`date -d "15 day ago" +"%d\/%m\/%Y"`
istore_day=`echo "${store_day}" | cut -c5-6`


if [ "${istore_day}"x == "01"x ];then
        k="Jan"
	nstore_day=`date -d "15 day ago" +"%d/""${k}""/%Y"`
        store_day=`date -d "15 day ago" +"%d\/""${k}""\/%Y"`
elif [ "${istore_day}"x == "02"x ];then
        k="Feb"
	nstore_day=`date -d "15 day ago" +"%d/""${k}""/%Y"`
        store_day=`date -d "15 day ago" +"%d\/""${k}""\/%Y"`
elif [ "${istore_day}"x  == "03"x ];then
        k="Mar"
	nstore_day=`date -d "15 day ago" +"%d/""${k}""/%Y"`
        store_day=`date -d "15 day ago" +"%d\/""${k}""\/%Y"`
elif [ "${istore_day}"x  == "04"x ];then
        k="Apr"
	nstore_day=`date -d "15 day ago" +"%d/""${k}""/%Y"`
        store_day=`date -d "15 day ago" +"%d\/""${k}""\/%Y"`
elif [ "${istore_day}"x  == "05"x ];then
        k="May"
	nstore_day=`date -d "15 day ago" +"%d/""${k}""/%Y"`
        store_day=`date -d "15 day ago" +"%d\/""${k}""\/%Y"`
elif [ "${istore_day}"x  == "06"x ];then
        k="Jun"
	nstore_day=`date -d "15 day ago" +"%d/""${k}""/%Y"`
        store_day=`date -d "15 day ago" +"%d\/""${k}""\/%Y"`
elif [ "${istore_day}"x  == "07"x ];then
        k="Jul"
	nstore_day=`date -d "15 day ago" +"%d/""${k}""/%Y"`
        store_day=`date -d "15 day ago" +"%d\/""${k}""\/%Y"`
elif [ "${istore_day}"x  == "08"x ];then
        k="Aug"
	nstore_day=`date -d "15 day ago" +"%d/""${k}""/%Y"`
        store_day=`date -d "15 day ago" +"%d\/""${k}""\/%Y"`
elif [ "${istore_day}"x  == "09"x ];then
        k="Sep"
	nstore_day=`date -d "15 day ago" +"%d/""${k}""/%Y"`
        store_day=`date -d "15 day ago" +"%d\/""${k}""\/%Y"`
elif [ "${istore_day}"x  == "10"x ];then
        k="Oct"
	nstore_day=`date -d "15 day ago" +"%d/""${k}""/%Y"`
        store_day=`date -d "15 day ago" +"%d\/""${k}""\/%Y"`
elif [ "${istore_day}"x  == "11"x ];then
        k="Nov"
	nstore_day=`date -d "15 day ago" +"%d/""${k}""/%Y"`
        store_day=`date -d "15 day ago" +"%d\/""${k}""\/%Y"`
else 
        k="Dec"
	nstore_day=`date -d "15 day ago" +"%d/""${k}""/%Y"`
        store_day=`date -d "15 day ago" +"%d\/""${k}""\/%Y"`
fi



grep "${nstore_day}"  access.log
if  [ $?  -eq  0 ];then
sed -i "1,/${store_day}/"d access.log
else
echo "日期不存在"
exit 0
fi
