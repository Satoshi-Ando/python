# coding:utf-8

import csv
import sys
import re

args = sys.argv

if len(sys.argv) < 2:
    print("-c:cjeck / -a:add")
    sys.exit()

option = args[1]



if option == '-a':
    no1 = input("Enter SR-Number:")
    no2 = input("Enter Pro/Lab/Jira:")
    no3 = input("Enter U/O:")
    no4 = input("Enter tr/QA:")

    write_data = [no1, no2, no3, no4]

    with open('SR.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(write_data)

elif option == '-c':
    f = open('SR.csv')
    data = f.readlines()
    num1 = input("Enter SR-Number:")

    for line in data:
        if line.find(num1) >= 0:
            print(line[:-1])

    f.close()

else:
    print("-c:cjeck / -a:add")

