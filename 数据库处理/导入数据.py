import pypyodbc,pymysql
mssqlcon = pypyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};SERVER=127.0.0.1;DATABASE=pacs;UID=sa;PWD=aaa111')
mysqlcon = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='aaa111', db='test', charset='utf8')
import datetime

def selectData(con,sql):
    cursor = con.cursor()
    cursor.execute(sql)
    row=cursor.fetchall()
    cursor.close()
    return row

'''
execute提供了直接传值
    value = [2,'John']
    cursor.execute('INSERT INTO test values(%s,%s)',value)
'''
def insertData(con,sql,value):
    cursor = con.cursor()
    cursor.execute(sql,value)
    con.commit()
    cursor.close()

'''
# 批量插入数据
    values = []
    for i in range(3, 20):
        values.append((i,'kk'+str(i)))
    cursor.executemany('INSERT INTO user values(%s,%s)',values)
'''
def insertManyData(con,sql,value):
    cursor = con.cursor()
    try:
        cursor.executemany(sql,value)
        con.commit()
        print("成功插入数据")
    except Exception as e:
        con.rollback()
        print("出错:"+str(e))
    finally:
        cursor.close()

'''
检查数据是否存在
'''
def check(con,sql,id):
    cursor = con.cursor()
    row=cursor.execute(sql,id)
    count=row.rowcount
    cursor.close()
    if count>0:
        return True
    else:
        return False

def main(start,end):
    start=datetime.datetime.strptime(start, "%Y-%m-%d")
    end = datetime.datetime.strptime(end, "%Y-%m-%d")
    days = (end - start).days+1
    for i in range(days):
        s1 = start+datetime.timedelta(days=i)
        s2 = start+datetime.timedelta(days=i+1)+datetime.timedelta(seconds=-1)
        selectStr = "select * from USWork where checktime>='%s' AND checktime<='%s' "%(s1,s2)
        print(selectStr)
        msdata = selectData(mssqlcon, selectStr)
        print('第%s天：%s条数据'%(str(i),str(len(msdata))))
        #insertsql = "insert into USWork values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',%s,'%s')"
        insertsql = "insert into USWork values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        insertManyData(mysqlcon,insertsql,msdata)





if __name__=="__main__":
    start = '2016-01-01'
    end = '2017-12-01'
    main(start,end)