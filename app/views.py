# -*- coding: utf-8 -*-
"""
用于携带页面主逻辑
"""
from flask_login import login_user, login_required, logout_user
from app import app
from flask import Flask, request, render_template, redirect, url_for, flash
from config import login_manager
from models import User
from dataInterface import getuserobj


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