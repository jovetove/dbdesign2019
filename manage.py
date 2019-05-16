"""
管理服务器运行的代码
"""
# -*- coding: utf-8 -*-
from flask_script import Manager, Server
from web import app

manager = Manager(app)
manager.add_command("runserver", Server(use_debugger=True))

if __name__ == '__main__':
    # manager.run()
    app.run(host='0.0.0.0', port=80, debug=True)
