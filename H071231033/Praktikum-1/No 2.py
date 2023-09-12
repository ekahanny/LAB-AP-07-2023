print('Konservasi Suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit')
c = int(input('Masukkan Suhu dalam Celcius : '))

k = c+273
r = int(4/5*c)
f = int((9/5*c)+32)

print(f"Hasil konversi dari suhu {c} derajat Celcius ke Kelvin adalah : {k}K ")
print(f"Hasil konversi dari suhu {c} derajat Celcius ke Kelvin adalah : {r}R ")
print(f"Hasil konversi dari suhu {c} derajat Celcius ke Kelvin adalah : {f}F ")