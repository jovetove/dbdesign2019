"""
配置代码
"""
from flask_login import LoginManager
from flask_cors import CORS, cross_origin
from web import app

cors = CORS(app, resources={r"/api":{"origins": "*"} })
app.config['CORS_HEADERS'] = 'Content-Type'

app.secret_key = 'dfgasdgvsadgv'
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.session_protection = 'strong'
login_manager.login_message = 'Access denied.'
login_manager.init_app(app)