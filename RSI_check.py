import re

file_name = "C:/Users/z2085102/Desktop/temp/python/log/RSI.txt"


file = open(file_name)
lines = file.readlines()
k = '-----------'
lines_strip = [line.strip() for line in lines]

l_001_i = [i for i, line in enumerate(lines_strip) if 'show chassis alarms' in line]
l_002_i = [i for i, line in enumerate(lines_strip) if 'show system core-dumps' in line]
l_003_i = [i for i, line in enumerate(lines_strip) if 'show chassis environment' in line]
l_004_i = [i for i, line in enumerate(lines_strip) if 'show chassis hardware detail' in line]
l_005_i = [i for i, line in enumerate(lines_strip) if 'show version detail' in line]


a001 = l_001_i[0]
b001 = l_001_i[1]
a002 = l_002_i[0]
b002 = l_002_i[1]
a003 = l_003_i[0]
b003 = l_003_i[1]
a004 = l_004_i[0]
b004 = l_004_i[1]
a005 = l_005_i[0]

print(k)
print(*lines_strip[a005:a005+5],sep="\n")
print(k)
print(*lines_strip[a001:a001+5],sep="\n")
print(k)
print(*lines_strip[b001:b001+5],sep="\n")
print(k)
print(*lines_strip[a002:a002+5],sep="\n")
print(k)
print(*lines_strip[b002:b002+5],sep="\n")
print(k)
print(*lines_strip[a003:a003+32],sep="\n")
print(k)
#print(*lines_strip[b003:b003+32],sep="\n")
#print(k)
print(*lines_strip[a004:a004+50],sep="\n")
print(k)
#print(*lines_strip[b004:b004+50],sep="\n")
#print(k)

file.close()


