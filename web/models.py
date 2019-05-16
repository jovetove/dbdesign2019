from flask_login import UserMixin
# from dataInterface import getuserobj
"""
登陆类模型
"""
class User(UserMixin):
    """
    继承UserMixin
    """
    def __init__(self):
        self.id = None
        self.password = None
        self.type = None