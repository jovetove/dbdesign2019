import attr

class api:
    """
    1. __init__
    2. 将dict_info 传入InterfaceJudgment 判断函数类型
    3. 使用相应的函数，查询数据，给相应的函数赋值
    test_data = {
    'api_name': 'stu_info',
    'params': {
        'sort': True,
        'number': 3
    },
    'fields': "id,name,shu"
    }

    做一个约定，我们的API接口名字，就为API函数的名字
    """

    def __init__(self, dict_info):
        self.dict_info = dict_info
        self.data = "0"
        self.InterfaceJudgment()

    def InterfaceJudgment(self):
        print(self.dict_info)
        funclist = ["stuinfo"]
        if self.dict_info['api_name'] in funclist:
            getattr(self, self.dict_info['api_name'])() # 使用字符串动态调用函数

    def stuinfo(self):
        self.data = '成功'
