a = str(input("Masukkan kata = "))

huruf1 = a[:1]
huruftengah = a[(len(a)//2)]
hurufakhir = a[-1:]

if len(a) % 2 == 0:
    huruftengah =  a[(len(a)//2)-1] + a[(len(a)//2)]  

hasil = huruf1 + huruftengah + hurufakhir
print(hasil)