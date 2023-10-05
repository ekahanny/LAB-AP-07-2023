x =int(input("masukkan nilai: "))
suku =[0,1]

while len(suku)<x:

 angka_selanjutnya= suku[-1]+ suku[-2]

 suku.append(angka_selanjutnya)

if x<=0:print('tidak valid')
elif x==1:print(0)
else:
 for angka in suku:
  print(angka,end=' ')
  



    

