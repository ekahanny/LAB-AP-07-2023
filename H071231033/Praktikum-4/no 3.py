def nilai_terbesar(daftar_angka):
    angka_besarpaling = daftar_angka[0]
    for angka in daftar_angka:
        if angka > angka_besarpaling:
            angka_besarpaling = angka
    return angka_besarpaling

daftar_angka = [-3, -45, -22, -10]
print(nilai_terbesar(daftar_angka))  # Output: 45