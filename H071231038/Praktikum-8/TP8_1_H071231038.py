import re

string = input('Masukkan string:\n')
pola = '^[A-Z|a-z|02468]{40}[13579|\s]{5}$'
result = re.match(pola,string)

if result:
    print(True)
else:
    print(False)

