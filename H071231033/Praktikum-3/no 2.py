def hitung_kembalian(total_belanja, uang_pembeli):
    denominasi = [100000, 50000, 20000, 10000, 5000, 2000, 1000]  # Daftar denominasi uang
    kembalian = uang_pembeli - total_belanja  # Menghitung jumlah kembalian
    if kembalian < 0:
        return "Uang pembeli tidak cukup"
    else:
        hasil = {}
        for d in denominasi:
            if kembalian >= d:
                hasil[d] = kembalian // d
                kembalian = kembalian % d
            else:
                hasil[d] = 0
        return hasil

total_belanja = int(input())
uang_pembeli = int(input())
hasil = hitung_kembalian(total_belanja, uang_pembeli)
for d in hasil:
    print(str(hasil[d]) + " uang sejumlah Rp." + str(d))

# harga_barang=int(input())
# uang_dibayar=int(input())

# def kembalian():
#     kembalian=uang_dibayar-harga_barang
#     pecahan_uang=[100000, 50000, 20000, 10000, 5000, 2000, 1000]
#     for pecahan in pecahan_uang:
#         jumlah=kembalian//pecahan
#         print(f'{jumlah}, uang sejumlah Rp.{pecahan}')
#         kembalian -= jumlah*pecahan

# kembalian()