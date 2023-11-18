angka = list(map(int,input("Masukkan beberapa angka: ").split())) #[1, 2, 3, 4]

angka_genap = []
angka_ganjil = []
angka_yang_habis_dibagi_5 = []

for i in angka: #1 2 3 4
    if i % 2==0:
        angka_genap.append(i)
    else:
        angka_ganjil.append(i)
    if i % 5 == 0:
        angka_yang_habis_dibagi_5.append(i)
print("Angka Ganjil: ", angka_ganjil)
print("Angka Genap: ", angka_genap)
print("Angka yang habis dibagi 5: ", angka_yang_habis_dibagi_5)