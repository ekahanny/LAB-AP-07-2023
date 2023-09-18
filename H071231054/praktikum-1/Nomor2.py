# mengubah suhu
print("Konversi suhu dari Celcius ke Kelvin, Reamur, dan Fahrenheit")
c = float(input("Masukkan nilai celcius: "))

print(f"Suhu dalam Kelvin: {c + 273:.0f}K")
print(f"Suhu dalam Reamur: {c*(4/5):.0f}°R")
print(f"Suhu dalam Fahrenheit: {c*(9/5)+32:.0f}°F")