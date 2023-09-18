print("pengujian jenis karakter")
print("-"*20)

a = (input("karakter : "))

huruf_kapital = a.isupper()
print("Huruf Kapital : " , huruf_kapital)
huruf_kecil = a.islower()
print("Huruf kecil : " , huruf_kecil)
angka = a.isdigit()
print("Angka :" , angka)