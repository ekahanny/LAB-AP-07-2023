import re

string = input()
if len(string) == 45:
    match = re.search(r'^[A-z02468]{40}[13579\s]{5}$',string)
    print(True)
else:
    print(False)