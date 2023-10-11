kata1=input('Masukkan Kata Pertama : ').lower().replace(' ','')
kata2=input('Masukkan Kata Kedua : ').lower().replace(' ','')

for huruf in kata1:
    hasil1=kata1.count(huruf)
    hasil2=kata2.count(huruf)
    if hasil1 == hasil2:
        continue
    else:
        print(False)
        break
    
if hasil1==hasil2:
    print(True)