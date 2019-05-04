# from app import connectMysql
import connectMysql

"""这个模块主要用于接受put回来的参数
并根据参数类型，return 相应的数据库里面的数据
"""


def getstuinfo(stu_id=None):
    """
    API接口函数
    接受学生ID return 学生tuple信息
    :param stu_id:
    :return:
    """
    dbobj = connectMysql.connectMysql()
    data = []
    if stu_id is None or len(stu_id) == 0:
        data = dbobj.select_db(sql="select * from student")
    else:
        for _id in stu_id:
            datastu = dbobj.select_db(sql="select * from student where ID = %s;" % _id)
            if len(datastu) != 0:
                data.append(datastu[0])
            else:
                print('%s 未查询到数据' % _id)
    dbobj.close_db()
    return data


def getuserobj(user_id=None):
    """
    登录查询用户是否存在的专用接口函数
    :param user_id: 用户id(username)
    :return:  if exit: return 用户对象
            else return None
    """
    dbobj = connectMysql.connectMysql()
    if user_id is '' or user_id is None:
        dbobj.close_db()
        return None
    else:
        userdata = dbobj.select_db(sql="select * from secret where ID = %s " % user_id)
    if userdata is ():
        # print("ID = %s and password = %s 未查询到数据" % (user_id, password))
        dbobj.close_db()
        return None
    else:
        dbobj.close_db()
        return userdata[0]


if __name__ == '__main__':
    pass
