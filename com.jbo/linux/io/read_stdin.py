# -*- coding: utf-8 -*-
from __future__ import print_function
import sys

for line in sys.stdin:
    print(line, end="")

#cat /etc/passwd | python read_stdin.py
#python read_stdin.py < /etc/passwd