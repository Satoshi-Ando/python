# coding: utf-8 #

import os
import glob

# windows の場合、row を宣言すればパス記述が楽
filepath = r'.\log\teraterm.log'

basename = os.path.basename(filepath)
print(basename)

# file名を元に別の名前をつけた
result = '{}_result.txt'.format(basename)
print(result)

k = '----------------------------------------------'
print(k)

files = glob.glob(r'.\log\*')
for name in files:
    file_name = name

basename1 = os.path.basename(file_name)
print(basename1)
print(k)

file_ext = os.path.splitext(basename1)

print(file_ext)
print(file_ext[0])
print(file_ext[1])

print(k)

# やりたいことができた。
basename2 = file_ext[0]
result1 = '{}_result.txt'.format(basename2)
print(result1)