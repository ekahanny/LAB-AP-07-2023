def kucing_tikus(K1,K2, t):
    jarak_K1 = abs(K1-t)
    jarak_K2 = abs(K2-t)
    if jarak_K1 == jarak_K2:
        return ' MOUSE C'
    elif jarak_K1 > jarak_K2:
        return 'CAT B'
    else:
        return'CAT A'
    

    print('masukkan jarak kucing A,B dan Tikus C')
try:
        jarak_kucing1 = int(input('CAT A = '))
        jarak_kucing2 = int(input('CAT B = '))
        jarak_tikus = int(input('MOS C = '))
        print()
        (f'CAT and MOUSE(CAT A = {jarak_kucing1},CAT B = {jarak_kucing2},MOUSE C = {jarak_tikus})')
        print(kucing_tikus(jarak_kucing1,jarak_kucing2,jarak_tikus))
except ValueError as pesan:
    print('Terjadi kesalahan =', pesan)