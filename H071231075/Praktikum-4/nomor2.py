def palindrom(kalimat:str) -> str :
    kalimat_kecil = kalimat . lower()
    kalimat_terbalik = kalimat_kecil[::-1]
    if kalimat_kecil == kalimat_terbalik:
        return 'palindrom'
    else:
        return 'bukan palindrom'
    

kalimat = input('masukkan sebuah string= ')
# print(f'palindrom({kalimat})')
print(palindrom(kalimat))
