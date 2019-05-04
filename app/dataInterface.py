# from app import connectMysql
import connectMysql

"""这个模块主要用于接受put回来的参数
并根据参数类型，return 相应的数据库里面的数据
"""


# 接受学生ID return 学生信息
def getstuinfo(stu_id=None):
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




def getuserinfo(user_id= None, password= None):

    """
    # 更具ID 查询数据库中用户id和密码是否存在，
    #
    # 如果不存在返回Type = None,存在 Type = ‘XXX’
    # user_id 和password 都为列表
    {
        MANAGER TECHER STUDENT
    }
    data 为存储用户信息元组的列表
    """
    #print(user_id, password)
    dbobj = connectMysql.connectMysql()
    if user_id is '' or password is '' :
        # data = dbobj.select_db(sql="select * from secret")
        return None
    else:
        # print('else')
        userdata = dbobj.select_db(
            sql="select * from secret where ID = %s and Password = %s;" % (user_id, password))
        # print(userdata)
        if userdata is ():
            # print("ID = %s and password = %s 未查询到数据" % (user_id, password))
            return None
        else:
            return userdata[0]


def getuserobj(user_id=                None):
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
        userdata = dbobj.select_db(
            sql="select * from secret where ID = %s " % (user_id)
        )
    if userdata is ():
        # print("ID = %s and password = %s 未查询到数据" % (user_id, password))
        dbobj.close_db()
        return None
    else:
        dbobj.close_db()
        return userdata[0]


if __name__ == '__main__':
    # stu_id = ['2017010002', '20170101001']
    a = getstuinfo(stu_id=[])
    for row in a:
        print(row)
    id = '2017010103'
    w  = '66666'
    b = getuserinfo(user_id=str(id), password=str(w))
    #b = getuserinfo(user_id='20170101003', password='666666')
    print('b:', b)
    #print('password:', b[1])
