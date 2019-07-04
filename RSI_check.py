# -*- coding: utf-8 -*-

import re
import os
import glob
import codecs
import shutil

files = glob.glob(r'.\log\*')
for name in files:
    file_name = name

file = open(file_name)
lines = file.readlines()
k = '--------------------------------------'
lines_strip = [line.strip() for line in lines]
line_show_list = [i for i, line in enumerate(lines_strip) if 'show ' in line]

l_001_i = [i for i, line in enumerate(lines_strip) if 'show version detail' in line]
l_002_i = [i for i, line in enumerate(lines_strip) if 'show chassis alarms' in line]
l_003_i = [i for i, line in enumerate(lines_strip) if 'show system core-dumps' in line]
l_004_i = [i for i, line in enumerate(lines_strip) if 'show chassis environment' in line]
l_005_i = [i for i, line in enumerate(lines_strip) if 'show chassis hardware detail' in line]

basename1 = os.path.basename(file_name)
file_ext = os.path.splitext(basename1)
basename2 = file_ext[0]
result1 = '{}_result.txt'.format(basename2)

open(result1,'w')

for no1_c in range(len(l_001_i)):
	no1_list = line_show_list.index(l_001_i[no1_c])
	no1_list_e = no1_list + 1
	print(k, file=codecs.open(result1, 'a', 'utf-8'))
	print(*lines_strip[line_show_list[no1_list]:line_show_list[no1_list_e]], sep="\n", file=codecs.open(result1, 'a', 'utf-8'))

for no2_c in range(len(l_002_i)):
	no2_list = line_show_list.index(l_002_i[no2_c])
	no2_list_e = no2_list + 1
	print(k, file=codecs.open(result1, 'a', 'utf-8'))
	print(*lines_strip[line_show_list[no2_list]:line_show_list[no2_list_e]], sep="\n", file=codecs.open(result1, 'a', 'utf-8'))

for no3_c in range(len(l_003_i)):
	no3_list = line_show_list.index(l_003_i[no3_c])
	no3_list_e = no3_list + 1
	print(k, file=codecs.open(result1, 'a', 'utf-8'))
	print(*lines_strip[line_show_list[no3_list]:line_show_list[no3_list_e]], sep="\n", file=codecs.open(result1, 'a', 'utf-8'))

for no4_c in range(len(l_004_i)):
	no4_list = line_show_list.index(l_004_i[no4_c])
	no4_list_e = no4_list + 1
	print(k, file=codecs.open(result1, 'a', 'utf-8'))
	print(*lines_strip[line_show_list[no4_list]:line_show_list[no4_list_e]], sep="\n", file=codecs.open(result1, 'a', 'utf-8'))

for no5_c in range(len(l_005_i)):
	no5_list = line_show_list.index(l_005_i[no5_c])
	no5_list_e = no5_list + 1
	print(k, file=codecs.open(result1, 'a', 'utf-8'))
	print(*lines_strip[line_show_list[no5_list]:line_show_list[no5_list_e]], sep="\n", file=codecs.open(result1, 'a', 'utf-8'))

shutil.move(result1, "C:/Users/z2085102/Desktop/")

file.close()