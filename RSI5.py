import re

file_name = "./RSI.txt"


file = open(file_name)
lines = file.readlines()

lines_strip = [line.strip() for line in lines]

#l_XXX = [line for line in lines_strip if 'show chassis alarms' in line]
#print(l_XXX)

l_XXX_i = [i for i, line in enumerate(lines_strip) if 'show chassis alarms' in line]
print(lines[l_XXX_i])


#for line in lines:
#  if re.search('show', line):
# 	 print(line, end="")

file.close()