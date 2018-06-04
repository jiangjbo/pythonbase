# -*- coding: utf-8 -*-
import hashlib
import json

import requests

__title__ = 'pyent'
__version__ = '0.1'


class Auth(object):
    def __init__(self, console_url, username, password):
        self.console_url = console_url
        self.username = username
        self.password = password

    def login(self):
        console_url = self.console_url
        username = self.username
        password = self.password
        user_agent = '{0}/{1}'.format(__title__, __version__)

        login_url = console_url + '/system/auth/login'
        with requests.session() as session:
            session.headers.update({'user-agent': user_agent})
            session.headers.update({'referer': console_url})
            # session.headers.update({'Content-Encoding': 'UTF-8'})

            m = hashlib.md5()
            m.update(password)
            data = {"username": username, "password": m.hexdigest(), "internal_bypass": True}
            # verify=False 取消证书验证
            response = session.post(login_url, json=data, verify=False)
            response_content = json.loads(response.content)
            session.headers.update({"TOKEN": response_content['data']['token']})
            session.cookies.set("TOKEN", response_content['data']['token'])
            print response_content['data']['token']
            session.verify = False
        return session


DEFAULT_USERNAME = 'admin'
DEFAULT_PASSWORD = 'S3cur!ty'
CONSOLE_URL_FORMAT = 'https://172.16.106.24'

auth = Auth(CONSOLE_URL_FORMAT, DEFAULT_USERNAME, DEFAULT_PASSWORD)
session = auth.login()
response = session.post(CONSOLE_URL_FORMAT + "")
response_content = json.loads(response.content)
