input_angka = (input("Masukkan beberapa angka: ")).split()

list_genap = [int(angka) for angka in input_angka if int(angka) % 2 == 0]
list_ganjil = [int(angka) for angka in input_angka if int(angka) % 2 != 0]
list_5 = [int(angka) for angka in input_angka if int(angka) % 5 == 0]

print(f"Angka genap: {list_genap}")
print(f"Angka ganjil: {list_ganjil}")
print(f"Angka yang habis dibagi 5: {list_5}")