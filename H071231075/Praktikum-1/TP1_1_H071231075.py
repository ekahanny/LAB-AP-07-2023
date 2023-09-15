x = float(input("masukkan nilai x : "))
y = float(input("masukkan nilai y :"))

z = ( x ** 2 + y** 2  ) ** 0.5

luas = (1/2 * y * x)
keliling = (x + y + z)

print(f"luas segitiga : {luas : .2f}")
print(f"Keliling Segitiga : {keliling :.2f}")

