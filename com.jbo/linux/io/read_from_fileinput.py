# -*- coding: utf-8 -*-

from __future__ import print_function
import fileinput
for line in fileinput.input():
    print(line, end="")

#cat /etc/passwd | python read_from_fileinput.py
#python read_from_fileinput.py < /etc/passwd
#python read_from_fileinput.py  /etc/passwd /etc/hosts