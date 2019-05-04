import pymysql

class connectMysql(object):
    """
    封装mysql操作类
    """

    def __init__(self, host='39.108.228.47', user='XiaoFa', passwd="SCU2019", dbname='StuManager'):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbname = dbname

        self.db = pymysql.connect(self.host, self.user, self.passwd, self.dbname)  # 连接数据库



    def select_db(self, sql):
        """ 数据库查询 """
        self.cursor = self.db.cursor()

        try:

            self.cursor.execute(sql)  # 返回 查询数据 条数 可以根据 返回值 判定处理结果
            data = self.cursor.fetchall()  # 返回所有记录列表
            # 结果遍历
            # for row in data:
            #     print(row)
            return data
        except:
            print('Error: unable to fecth data')
        finally:
            self.cursor.close()


    def insert_db(self, sql):
        """ 插入数据库操作 """
        self.cursor = self.db.cursor()
        try:
            # 执行sql
            self.cursor.execute(sql)
            # tt = self.cursor.execute(sql)  # 返回 插入数据 条数 可以根据 返回值 判定处理结果
            # print(tt)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()


    def delete_db(self,sql):
        """ 操作数据库数据删除 """
        self.cursor = self.db.cursor()

        try:
            # 执行sql
            self.cursor.execute(sql)
            # tt = self.cursor.execute(sql) # 返回 删除数据 条数 可以根据 返回值 判定处理结果
            # print(tt)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()


    def update_db(self, sql):
        """ 更新数据库操作 """
        self.cursor = self.db.cursor()
        try:
            # 执行sql
            self.cursor.execute(sql)
            # tt = self.cursor.execute(sql) # 返回 更新数据 条数 可以根据 返回值 判定处理结果
            # print(tt)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()


    def close_db(self):
        ''' 数据库连接关闭 '''
        self.db.close()