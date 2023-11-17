kata=input('Masukkan Kata : ').replace(' ','')

panjang_kata=len(kata)
kata2=kata[0]+kata[(panjang_kata//2)]+kata[-1]

if len(kata)< 3:
    print('error')
else:
    print(kata2)