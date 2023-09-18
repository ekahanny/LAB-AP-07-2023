print("Konversi detik ke jam")

inputan_detik = int(input("masukkan jumlah detik: "))
jam = inputan_detik // 3600
sisa_detik = (inputan_detik - (jam * 3600))
menit = sisa_detik // 60
detik = sisa_detik - (menit * 60)

print(f"{jam:02}:{menit:02}:{detik:02}")