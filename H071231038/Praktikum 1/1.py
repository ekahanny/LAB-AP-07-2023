print("Menghitung luas dan keliling segitiga")

x = int(input("Panjang sisi X: "))
y = int(input("Panjang sisi Y: "))
z = (x**2 + y**2)**0.5
print(f"Panjang sisi Z: {z:.2f}")

Luas = 0.5 * x * y
print(f"Luas Permukaan = {Luas:.2f}")
Keliling = x +y + z
print(f"Keliling = {Keliling:.2f}")