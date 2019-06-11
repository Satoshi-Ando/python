import re

file_name = "./RSI.txt"


file = open(file_name)
lines = file.readlines()
lines_strip = [line.strip() for line in lines]
print(lines_strip)
print(lines_strip[2:4])

file.close()