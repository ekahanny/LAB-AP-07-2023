hargabarang = int(input("Harga : "))
dibayar = int(input("Dibayar : "))

kembalian = dibayar - hargabarang
if kembalian < 0 :
    print("uang kurang")
else:
    pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

    for variabel in range(0, 7):
        
        jumlah = kembalian // (pecahan[variabel])
        kembalian -= jumlah * (pecahan[variabel])
        print(f"{jumlah} uang sejumlah Rp.{pecahan[variabel]}")