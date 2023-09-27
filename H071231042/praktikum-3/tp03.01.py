
n = int(input("Masukkan nilai N : "))
if n < 0:
    print("Bukan angka fibonacci") #Syarat Bilangan Fibonacci tidak mines atau 0!
else:
    s1 = 0 #Suku pertama bilangan fibonacci
    s2 = 1 #Suku kedua bilangan fibonacci
    for i in range(n): #Perulangan dari index ke 2 sampai ke n
        print(s1, end=" ")
        s3 = s1+s2
        s1 = s2
        s2 = s3
        
