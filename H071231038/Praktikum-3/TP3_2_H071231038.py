harga = int(input("harga barang = "))
bayar = int(input("bayar = "))
kembalian = int(bayar - harga)
print(f"kembalian = {kembalian}")
for pecahan in [100000,50000,20000,10000,5000,2000,1000,500,200,100]:
    jumlahpecahan = (kembalian // pecahan)
    kembalian = kembalian - (pecahan*jumlahpecahan)
    print(f"{jumlahpecahan} uang sejumlah Rp.{pecahan}")
   