# -*- coding: utf-8 -*-
"""
用于携带页面主逻辑
"""
import simplejson
from flask_cors import cross_origin
from flask_login import login_user, login_required, logout_user
from web import app
from flask import Flask, request, render_template, redirect, url_for, flash, jsonify, json, send_from_directory, \
    make_response
from config import login_manager
from web.models import User
from web.dataInterface import getuserobj
import web.api

@login_manager.user_loader
def load_user(user_id):
    """
    :param user_id: 用户id
    :return: 如果存在该用户，返回该用户的信息元组
    """
    userobj = getuserobj(user_id)
    if userobj is not None:
        curr_user = User()
        curr_user.id = userobj[0]
        curr_user.password = userobj[1]
        curr_user.type = userobj[2]
        return curr_user


# 登录页面 主页面
@app.route('/', methods=['GET', 'POST'])
def login():
    # 最开始请求为GET 故第一次请求会 直接 return render_template('login.html')
    if request.method == 'POST':
        user_id = request.form.get('username')
        user_password = request.form.get('password')
        curr_user = load_user(user_id)  # 注册用户
        if curr_user is not None:
            if curr_user.password != user_password:
                logout_user()  # 密码错误注销用户
                return render_template('login.html')
            elif curr_user.password == user_password:
                # 后面需要根据账号类型 分别转向不同的页面
                if curr_user.type == 'STUDENT':
                    return render_template('stu_index.html')
                elif curr_user.type == 'TECHER':
                    return render_template('tea_index.html')
                elif curr_user.type == 'MANAGER':
                    return render_template('man_index.html')
            flash('Wrong username or password!')
    # GET 请求
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out successfully!'


def fullResponse(statu_dic, data):
    return jsonify({'status': statu_dic, 'data': data})


R200_OK = {'code': 200, 'message': 'OK all right.'}
test_data = {
    'api_name': 'stu_info',
    'params': {
        'sort': True,
        'number': 3
    },
    'fields': "id,name,shu"
}


@app.route('/api', methods=['GET', 'POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization']) # 允许跨域请求
def api_data():
    try:
        postdata = json.loads(request.get_data(as_text=True))  # 将bytes转换为Unicode,再转化为json的dict
    except simplejson.errors.JSONDecodeError:
        return "输入的格式非Json！"
    check_key = "dict_keys(['api_name', 'params', 'fields'])"  # 用于验证json 的键值是否正确
    if str(postdata.keys()) != check_key:
        promptstring = "输入的json格式错误！"
        return promptstring
    return web.api.api(postdata).data

@app.route('/nohup.out')
def robots():
    response = make_response(open('nohup.out').read())
    response.headers["Content-type"] = "text/html"
    return response
    # return send_from_directory('', 'nohup.out')