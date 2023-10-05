def permutasi_kata(kata):
    try:
        hasil = ''
        for i in range(len(kata)):
         kata_mutasi = kata[-1] + kata[:-1]
         hasil = hasil + kata_mutasi + ' | '
         kata = kata_mutasi
        return(hasil)

    except TypeError as pesan:
        return'terjadi kesalahan =', pesan


kata_input = input('masukkan sebuah kata = ')
print(f'string permutation({kata_input})')
print(permutasi_kata(kata_input))