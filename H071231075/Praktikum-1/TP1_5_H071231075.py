print("konversi detik ke jam, menit dan detik ")

s = int(input("Masukkan detik: "))

jam = s//3600
menit = (s-(jam*3600))//60
detik = (s-(jam*3600)-(menit*60))

print(f"{jam:02d}:{menit:02d}:{detik:02d}")