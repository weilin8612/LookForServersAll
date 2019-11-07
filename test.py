import re


str = '● ├─accounts-daemon.service'

table = str.maketrans('● ├─', '    ')
print(table)
result = str.translate(table)
print(result)
print(str)
# pr = re.compile(r'dae')
# result = pr.match(str)
#
# print(type(result))

