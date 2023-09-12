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
