# menghitung luas dan keliling
print("Menghitung Luas Permukaan dan Keliling")
x = int(input("Masukkan panjang sisi x (Tinggi) : "))
y = int(input("Masukkan panjang sisi y (Alas) : "))
z = (x**2 + y**2)**0.5

Luas = (1/2 * y) * x
Keliling = (x + y + z)

print(f"Luas dari segitiga : {Luas:.2f}")
print(f"Keliling dari segitiga : {Keliling:.2f}")