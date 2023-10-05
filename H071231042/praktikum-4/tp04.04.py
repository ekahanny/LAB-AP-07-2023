def catAndMouse(catA, catB, mouseC):
    a = (catA - mouseC)**2
    b = (catB - mouseC)**2
    if a > b :
        print("cat B")
    elif a < b :
        print("cat A")
    elif a == b :
        print("mouse C")

catA = int(input("masukkan jarak cat A : "))
catB = int(input("masukkan jarak cat B : "))
mouseC = int(input("masukan jarak mouse C : "))
catAndMouse(catA, catB, mouseC)