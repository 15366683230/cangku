import pymysql




#创建数据库表

def create_database():

    #数据库信息
    conn = pymysql.connect(host = '127.0.0.1', port = 3306,
                           user = 'root', password = '120993988',db = 'cangku',
                           charset = 'utf8')

    #创建游标
    cursor = conn.cursor()


    #创建表、添加字段
    sql_add_table = 'create table `fixed_assets`(id int not null key auto_increment)'
    sql_insert0= 'alter table `fixed_assets` add 资产编号 int not null unique '
    sql_insert1 = 'alter table `fixed_assets` add  类型 varchar(20) not null '
    sql_insert2 = 'alter table `fixed_assets` add  资产名称 varchar(20) not null '
    sql_insert3 = 'alter table `fixed_assets` add  事件类型 varchar(20) not null '
    sql_insert4 = 'alter table `fixed_assets` add  责任处室 varchar(20) not null '
    sql_insert5 = 'alter table `fixed_assets` add  责任人 varchar(20) not null '
    sql_insert6 = 'alter table `fixed_assets` add  员工编号 varchar(20) not null '
    sql_insert7 = 'alter table `fixed_assets` add  存放地点 varchar(40)'
    sql_insert8 = 'alter table `fixed_assets` add  工单号 varchar(20)'

    try:
        cursor.execute(sql_add_table)
        sql_list = [sql_insert0, sql_insert1, sql_insert2, sql_insert3, sql_insert4, sql_insert5,
                sql_insert6, sql_insert7, sql_insert8]
        for sql in sql_list:
            cursor.execute(sql)
        conn.commit()
        print('语句执行完成！')
    except Exception as e:
        conn.rollback()
        print('执行失败了！', e)


    cursor.close()
    conn.close()


create_database()

##############################################################################################
from  tkinter import *


from tkinter import messagebox, ttk


#创建固定资产号
#
# root = Tk()
# root.title('新建固定资产')
#
#
# lable =Label(root, text = '新建固定资产', font = "楷体", )
# lable.grid(anchor = NW)
#












# root.mainloop()