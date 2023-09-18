print("Konversi suhu dari Celcius ke Kelvin, Reamur, dan Fahrenheit")
c = float(input("Masukkan Suhu dalam Celcius = "))

k = c + 273.15
k_int = int(k)

r = (c * 4) / 5
r_int = int(r)

f = (c * 9/5) + 32
f_int = int(f)

print(f"Hasil konversi dari suhu {c} derajat Celcius ke Kelvin adalah : {k_int}K")
print(f"Hasil konversi dari suhu {c} derajat Celcius ke Reamur adalah : {r_int}R")
print(f"Hasil konversi dari suhu {c} derajat Celcius ke Fahrenheit adalah : {f_int}F")