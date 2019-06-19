#coding=utf-8
import pymysql
import xlwt
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

def get_conn():
    conn = pymysql.connect('192.168.126.100', port=3306, user='root', passwd='123456', db='test', charset='utf8')
    return conn

def query_all(cur, sql, args):
    cur.execute(sql, args)
    return cur.fetchall()

def read_mysql_to_xls(filename):
    list_table_head = ['序号', '类型', '是否有子级', '子级类型', '名字', 'goid', 'gourl', 'apply_url', '城市', '父级id','别名','修改时间','has_sx', 'has_cq']
    # 最大读取行数是65535
    workbook = xlwt.Workbook(encoding='utf-8') 
    sheet = workbook.add_sheet('data', cell_overwrite_ok = True)
    for i in range(len(list_table_head)):
        sheet.write(0, i ,list_table_head[i])
        
    conn = get_conn()
    cur = conn.cursor()
    sql = 'select * from sx_tree_1 limit 1'
    results = query_all(cur, sql, None)
    conn.commit()
    cur.close()
    conn.close()
    row = 1
    for result in results:
        col = 0
        print(type(result))
        print(result)
        for item in result:
            print(item)
            sheet.write(row, col, item)
            col += 1
        row += 1
        
    workbook.save(filename)
    
if __name__ == '__main__':
    read_mysql_to_xls('/root/python/test.xls')
