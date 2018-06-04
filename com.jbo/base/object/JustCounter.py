#!/usr/bin/python
# -*- coding: UTF-8 -*-

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print "私有变量", self.__secretCount

    def count2(self):
        print self.__secretCount

counter = JustCounter()
counter.count()
# 在类的对象生成后,调用含有类私有属性的函数时就可以使用到私有属性.
counter.count()

print "公开变量", counter.publicCount
print "私有变量", counter._JustCounter__secretCount

try:
    counter.count2()
except IOError:
    print "不能调用非公有属性!"
else:
    print "ok!"








