def angka_terbesar(*angka):
    terbesar = angka[0]
    for nomor in angka:
        if nomor > terbesar:
            terbesar = nomor
    return terbesar

print(angka_terbesar(37, 84, 29, 51, 12))

print(angka_terbesar(73, 93))

print(angka_terbesar(39, 76, 96, 27))

print(angka_terbesar(60, 85, 22, 56))