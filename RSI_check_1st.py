import re
import glob
import codecs

files = glob.glob(".\log\*")
for name in files:
	file_name = name

file = open(file_name)
lines = file.readlines()
k = '--------------------------------------'
lines_strip = [line.strip() for line in lines]

line_show_list = [i for i, line in enumerate(lines_strip) if 'show ' in line]
#print(line_show_list)

l_001_i = [i for i, line in enumerate(lines_strip) if 'show version detail' in line]
l_002_i = [i for i, line in enumerate(lines_strip) if 'show chassis alarms' in line]
l_003_i = [i for i, line in enumerate(lines_strip) if 'show system core-dumps' in line]
l_004_i = [i for i, line in enumerate(lines_strip) if 'show chassis environment' in line]
l_005_i = [i for i, line in enumerate(lines_strip) if 'show chassis hardware detail' in line]


#print(l_001_i)
no1 = len(l_001_i)
#print(no1)

for no1_c in range(len(l_001_i)):
	no1_list = line_show_list.index(l_001_i[no1_c])
	no1_list_e = no1_list + 1
	print(k)
	print(*lines_strip[line_show_list[no1_list]:line_show_list[no1_list_e]], sep="\n")

for no2_c in range(len(l_002_i)):
	no2_list = line_show_list.index(l_002_i[no2_c])
	no2_list_e = no2_list + 1
	print(k)
	print(*lines_strip[line_show_list[no2_list]:line_show_list[no2_list_e]], sep="\n")

for no3_c in range(len(l_003_i)):
	no3_list = line_show_list.index(l_003_i[no3_c])
	no3_list_e = no3_list + 1
	print(k)
	print(*lines_strip[line_show_list[no3_list]:line_show_list[no3_list_e]], sep="\n")

for no4_c in range(len(l_004_i)):
	no4_list = line_show_list.index(l_004_i[no4_c])
	no4_list_e = no4_list + 1
	print(k)
	print(*lines_strip[line_show_list[no4_list]:line_show_list[no4_list_e]], sep="\n")

for no5_c in range(len(l_005_i)):
	no5_list = line_show_list.index(l_005_i[no5_c])
	no5_list_e = no5_list + 1
	print(k)
	print(*lines_strip[line_show_list[no5_list]:line_show_list[no5_list_e]], sep="\n")


file.close()


