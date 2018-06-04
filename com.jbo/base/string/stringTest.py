# -*- coding: utf-8 -*-

s = "Hello,world"
print(len(s))
print("world" in s)
print("world" not in s)

li = [1, 2, 3, 4, 5]
print(len(li))
print(1 in li)

print(",", ["a", "b", "c"])

with open('data.txt') as inf, open('out.txt', 'w') as outf:
    for line in inf:
        outf.wirte(' '.join([word.capitalize() for word in line.split()]))
        outf.write("\n")

