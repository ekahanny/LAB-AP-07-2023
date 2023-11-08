import re
x = input("Masukkan String Anda : ")
pola = re.match(r"[A-Za-z02468]{40}([13579\s]{5})$", x)
if pola:
    print("True")
else:
    print("False")
