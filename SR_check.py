# coding:utf-8

import csv
import sys
import re

f = open('SR.csv')

data = f.readlines()

#for row in data:
#    print(row)


for line in data:
    if line.find(num1) >= 0:
       print(line[:-1])

f.close()