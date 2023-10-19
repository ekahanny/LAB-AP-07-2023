angka = input("masukkan beberapa angka :").split()
angka = list(map(int, angka))
genap = []
ganjil = []
habis5 = []
for i in angka:
    if i % 2 ==0:
        genap.append(i)
    elif i % 2 != 0:
        ganjil.append(i)
    if i % 5 == 0:
        habis5.append(i)

print(f" angka genap : {genap}")
print(f" angka ganjil : {ganjil}")
print(f" angka habis5 : {habis5}")