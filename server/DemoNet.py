#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from flask import jsonify
from model import User
import pymysql
from initsql import getUserDataByName, insertData, quitMysql

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        p_username = request.form.get('email', None)
        p_password = request.form.get('password', None)
        p_username = p_username.encode('utf-8')
        # query = User.query.filter_by(username=p_username).first()
        query = getUserDataByName(p_username)
        if query is "userIsNotExisted":
            response = {
                "error": "true",
                "error_msg": "用户名不存在，请注册！"
            }
        elif query is "failure":
            response = {
                "error": "true",
                "error_msg": "Error: unable to fetch data!"
            }
        else:
            if query.encrypted_password != p_password:
                response = {
                    "error": "true",
                    "error_msg": "用户密码错误！"
                }
            else:
                response = {
                    "error": "false",
                    "user": {
                        "name": query.name,
                        "email": query.email
                    }
                }
        return json.dumps(response, ensure_ascii=False)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        p_username = request.form.get('username', None)
        p_password = request.form.get('password', None)
        p_email = request.form.get('email', None)
        p_username = p_username.encode('utf-8')
        p_password = p_password.encode('utf-8')
        p_email = p_email.encode('utf-8')

        query = insertData(p_username,  p_email, p_password)
        if query == "userIsExisted":
            response = {
                "error": "true",
                "error_msg": "用户名已存在，请登录！"
            }
        elif query == "failure":
            response = {
                "error": "false",
                "error_msg": "注册失败！"
            }
        else:
            response = {
                "error": "false",
                "user": {
                    "name": p_username,
                    "email": p_email
                }
            }
        return json.dumps(response, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True)
