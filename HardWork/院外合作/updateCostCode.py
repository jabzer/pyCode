#!/usr/bin/python3
import pypyodbc

hlzy = "driver={IBM DB2 ODBC DRIVER};database=%s;hostname=%s;port=%s;protocol=tcpip;uid=%s;pwd=%s" % (
"hlzy", "10.11.0.12", "50005", "neusoft", "czDDJ16")
db2test = "driver={IBM DB2 ODBC DRIVER};database=%s;hostname=%s;port=%s;protocol=tcpip;uid=%s;pwd=%s" % (
    "db2test", "10.11.1.72", "57777", "neusoft", "neusoft")

isitect = "driver={IBM DB2 ODBC DRIVER};database=%s;hostname=%s;port=%s;protocol=tcpip;uid=%s;pwd=%s" % (
    "db2test", "10.11.1.72", "57777", "neusoft", "neusoft")


def testconnect(db2name):
    conStr = pypyodbc.connect(db2name)
    cursor = conStr.cursor()
    cursor.execute("SELECT * FROM COM_DEPARTMENT with ur ")
    row = cursor.fetchall()
    cursor.close()
    conStr.close()
    for r in row:
        print(r)


def SelSql(dbStr, sql):
    try:
        conn = pypyodbc.connect(dbStr)
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        print("获取到{}条数据".format(len(result)))
        cursor.close()
        conn.close()
        return result
    except Exception as e:
        print("--数据库连接问题:{0}".format(str(e)))
        return None





if __name__ == '__main__':
    #获得字典
    startdate = '2018-04-01 00:00:00'
    enddate = '2018-05-01 00:00:00'

    sql = "SELECT ITEM_CODE, COST_CODE FROM temp_dict_item with ur"
    dictItem = SelSql(isitect, sql)
    for itemCode,costCode in dictItem:
        recordsql = ''' SELECT a.RECIPE_NO,a.ITEM_NAME,a.ITEM_NAME,a.PACKAGE_CODE,a.COST_CODE FROM fin_opb_feedetail a 
                        WHERE a.PAY_FLAG ='1' AND a.CANCEL_FLAG != '3' 
                        AND  a.FEE_DATE >={0} AND a.FEE_DATE<{1}
                        AND a.PACKAGE_CODE={2}
                        AND a.COST_CODE<>{3}
                        WITH UR'''.format(startdate,enddate,itemCode,costCode)
        print(recordsql)
        SelSql(recordsql)


