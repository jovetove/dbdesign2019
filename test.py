"""
没什么卵用
用于简单的测试
"""
def func(strname = None,funcnumber = 0):
    print('id = '+ str(funcnumber) + ' is ' + strname)


if __name__ == '__main__':
    a = 'qwe'
    func(strname=a, funcnumber=0)
    func(strname='qwe',funcnumber=1)

