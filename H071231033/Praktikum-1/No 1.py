print('Menghitung luas permukaan dan keliling segitiga')
x = float(input('Panjang sisi X : '))
y = float(input('Panjang sisi Y : '))
z = (x**2+y**2)**(0.5)

luas = 0.5*x*y
keliling = x+y+z
print(f"Luas Permukaan {luas:.2f}")
print(f"Keliling {keliling:.2f}")