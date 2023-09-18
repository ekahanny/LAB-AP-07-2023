print("Konversi detik ke jam")
x = int(input("masukan detik: "))

jam = x//3600
menit = (x%3600)//60
detik = x%60

print(f"{jam:02d}:{menit:02d}:{detik:02d}")