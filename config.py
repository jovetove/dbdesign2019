"""
配置代码
"""
from flask_login import LoginManager

from app import app

app.secret_key = 'dfgasdgvsadgv'
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.session_protection = 'strong'
login_manager.login_message = 'Access denied.'
login_manager.init_app(app)