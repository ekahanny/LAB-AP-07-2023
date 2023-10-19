data = list(map(int, input('Masukkan beberapa angka : ').split()))

genap = [i for i in data if i % 2 == 0]
ganjil = [i for i in data if i % 2 != 0]
bagi5 = [i for i in data if i % 5 == 0]

print(f"Angka Genap : {genap}")
print(f"Angka Ganjil : {ganjil}")
print(f"Angka habis dibagi 5 : {bagi5}")