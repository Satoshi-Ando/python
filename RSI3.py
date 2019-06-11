import re

file_name = "./RSI.txt"


file = open(file_name)
lines = file.readlines()

for line in lines:
	if re.search('show chassis alarms', line):
		print(line, end="")

file.close()