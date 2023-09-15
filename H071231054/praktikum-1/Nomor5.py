# mengubah detik
print("konversi detik menjadi jam")
angka = int(input("masukkan jumlahn detik: "))

jam = angka // 3600
sisa_detik = angka % (jam * 3600)

menit = sisa_detik // 60
detik = sisa_detik % 60

print(f'{jam:02d}:{menit:02d}:{detik:02d}')