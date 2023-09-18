karakter = input("Masukkan karakter: ")

upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", 
         "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
         'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

kapital = karakter in upper
kecil = karakter in lower
angka = karakter in num

print("Huruf kapital?",kapital)
print("Huruf kecil?",kecil)
print("Angka?",angka)