# menghitung luas dan keliling
print("Menghitung Luas Permukaan dan Keliling")
x = int(input("Masukkan panjang sisi x (Tinggi) : "))
y = int(input("Masukkan panjang sisi y (Alas) : "))
z = (x**2 + y**2)**0.5

Luas = (1/2 * y) * x
Keliling = (x + y + z)

print(f"Luas dari segitiga : {Luas:.2f}")
print(f"Keliling dari segitiga : {Keliling:.2f}")

# mengubah suhu
print("Konversi suhu dari Celcius ke Kelvin, Reamur, dan Fahrenheit")
c = float(input("Masukkan nilai celcius: "))

print(f"Suhu dalam Kelvin: {c + 273:.0f}K")
print(f"Suhu dalam Reamur: {c*(4/5):.0f}°R")
print(f"Suhu dalam Fahrenheit: {c*(9/5)+32:.0f}°F")

# nilai x yang memenuhi persamaan
a = float(input("masukkan nilai a: "))
b = float(input("masukkan nilai b: "))
c = float(input("masukkan nilai c: "))

# menentukan karakter
if a!= 0:
    x1 = (-b+(b**2 - 4*a*c)**(1/2))/(2*a)
    x2 = (-b-(b**2 - 4*a*c)**(1/2))/(2*a)
    
    print(f'{x1:.2f}')
    print(f'{x2:.2f}')
else:
    print("a != 0")

x = input("masukkan character:")

kapital = x.isupper()
kecil = x.islower()
angka = x.isdigit()

print(f'huruf kapital: {kapital}')
print(f'huruf kecil: {kecil}')
print(f'angka: {angka}')

# mengubah detik
print("konversi detik menjadi jam")
angka = int(input("masukkan jumlahn detik: "))

jam = angka // 3600
sisa_detik = angka % (jam * 3600)

menit = sisa_detik // 60
detik = sisa_detik % 60

print(f'{jam:02d}:{menit:02d}:{detik:02d}')