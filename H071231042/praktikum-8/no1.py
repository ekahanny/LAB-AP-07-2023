import re
S = input("Masukkan String Anda : ")
panjang = re.match(r"[A-z0-9\S]{40}[13579\s]{5}$", S)
if panjang:
    print("True")
else:
    print("False")