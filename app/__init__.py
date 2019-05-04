# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)  # 创建Flask类的实例
app.config.from_object("config")  # 从config.py读入配置

# 这个import语句放在这里, 防止views, models import发生循环import
import views