# x1 = "Anak Band"
# x2 = "dakan ba"
x1 = input("masukan kata ke1 :")
x2 = input("masukan kata ke2 :")
x1 = x1.replace(" " , "").lower()
x2 = x2.replace(" " , "").lower()
kata1 = []
kata2 = []
for var in x1:
    angka1 = x1.count(var)
    angka2 = x2.count(var)
    kata1.append(angka1)
    kata2.append(angka2)
if  len(x1) == len(x2):
        if kata2 == kata1:
            print("True")
        else:
            print("False")
else:
    print("False")
