derajat = float(input("derajat = "))

while derajat > 360:
    print("invalid")
    derajat = float(input("derajat = "))

jam = derajat / 15
s = jam*3600 + 6*3600
j = s/3600

if derajat >= 270:
    j = j % 24

waktu = int(s)
j_int = int(j)
menit = (waktu % 3600) // 60
detik = waktu % 60   
a = f"{j_int:02}:{menit:02}:{detik:02}"

if j > 0 and j < 12:
    print("Selamat Pagi")
elif j >= 12 and j < 15:
    print("Selamat Siang")
elif j >= 15 and j < 19:
    print("Selamat Sore")
elif j >= 19 and j < 24:
    print("Selamat Malam")

print(a)