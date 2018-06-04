#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept()
    print '连接地址: ', addr
    c.send("hello world")
    c.close()
