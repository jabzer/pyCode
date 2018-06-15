#!/usr/bin/python3
import sys

with open('txt.txt', 'r',encoding='utf8') as f:
    allline = f.readlines()

linestr = []

for line in allline:
    line = "'{}'".format(line.replace('\n', '').replace(' ',''))
    if len(line) > 2:
        linestr.append(line)

out = ",".join(linestr)
print(out)
