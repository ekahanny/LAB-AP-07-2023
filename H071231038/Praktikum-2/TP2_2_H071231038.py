list_a = ["vertebrado", "invertebrado"]
a = str(input("Masukkan input pertama: "))
while a not in list_a:
    print("Invalid Input")
    a = str(input("Masukkan input pertama: "))


list_b = ["ave","mamifero","inseto","anelideo"]
b = str(input("Masukkan input kedua: "))
while b not in list_b:
    print("Invalid Input")
    b = str(input("Masukkan input kedua: "))

list_c = ["carnivoro","onivoro","herbivoro","hematofago"]
c = str(input("Masukkan input ketiga: "))
while c not in list_c:
    print("Invalid Input")
    c = str(input("Masukkan input ketiga: "))

if a == "vertebrado":
    if b == "ave":
        if c == "carnivoro":
            print("aguia")
        elif c == "onivoro":
            print("pomba")
        
    if b == "mamifero":
        if c == "onivoro":
            print("homem")
        elif c == "herbivoro":
            print("vaca")

elif a == "invertebrado":
    if b == "inseto":
        if c == "hematofago":
            print("pulga")
        elif c == "herbivoro":
            print("lagarta")
        
    if b == "anelideo":
        if c == "hematofago":
            print("sanguessuga")
        elif c == "onivoro":
            print("minhoca")
else:
    print("Invalid Input")
        
        