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



aa = {"pull_time": 1534933568703, "Category": "\t\xe5\xae\x89\xe5\x85\xa8 ID:\t\tS-1-5-21-1688866898-141319640-2308027785-1371"}
print aa
