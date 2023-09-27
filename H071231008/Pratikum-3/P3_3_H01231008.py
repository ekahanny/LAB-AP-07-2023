while True:
    try:
        derajat = float(input("Masukan Posisi Matahari (Derajat) : "))
    except ValueError:
        print ("Invalid Input")
        exit()
    if 0 <= derajat <=360:
        break

if derajat >= 0 and derajat <= 90: 
    Waktu = "Pagi"
elif derajat > 90 and derajat <= 180:
    Waktu = "Siang"
elif derajat > 180 and derajat <= 270:
    Waktu = "Sore"
else:Waktu = "Malam"

derajat *= 240
jam = int(derajat // 3600)+6
if jam >= 24:
    jam %= 24
menit = int(derajat % 3600 // 60)
derajat = int(derajat % 3600 % 60)
digicloak = (f"{jam:02}:{menit:02}:{derajat:02}")
print (f"Selamat {Waktu}\n{digicloak}")




