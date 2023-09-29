n = int(input())
suku1, suku2 = 0, 1
hitung = 0

if n <= 0:
    print("Masukkan bilangan bulat positif")
elif n == 1:
    print(suku1)
else:
    while hitung < n:
        print(suku1, end=" ")
        suku_ke_n = suku1 + suku2
        suku1 = suku2
        suku2 = suku_ke_n
        hitung = 1 + hitung