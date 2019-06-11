import re

file_name = "./RSI.txt"

try:
    file = open(file_name)
    data = file.read()
    print(data)

finally:
    file.close()