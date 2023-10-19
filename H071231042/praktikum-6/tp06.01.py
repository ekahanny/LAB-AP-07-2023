var = {"nama" : "", "umur" : "", "alamat" : ""}
print("Selamat datang untuk memulai silahkan input data anda")
nama = input("Input Nama : ")
var["nama"] = nama
umur = int(input("Input Umur : "))
var["umur"] = umur
alamat = input("Input Alamat : ")
var["alamat"] = alamat
#  dalam dictionery itu variabelnya , nama,umur,alamat adalah isinya 
while True:
    print(f"""
===================================================
Selamat datang {var['nama']} Silahkan pilih Opsi
===================================================
1. Detail Anda
2. Ubah Nama
3. Ubah Umur
4. Ubah Alamat
5. Keluar
===================================================""")
    opsi = int(input("Input Opsi : "))
    match opsi:
        case 1:
            print(f"""
===================================================
Data anda adalah
Nama : {var['nama']}
Umur : {var['umur']}
Alamat : {var['alamat']}""")
        case 2:
            var["nama"] = input(f"Silahkan Input Nama Baru : ")
            print("Data Anda Sukses Diperbarui")
        case 3:
            var["umur"] = input(f"Silahkan Input Umur Baru Anda : ")
            print("Data Anda Sukses Diperbarui")
        case 4:
            var["alamat"] = input(f"Silahkan Input Alamat Baru Anda :")
            print("Data Anda Sukses Diperbarui")
        case 5:
            print(f"Selamat Tinggal {var['nama']}")
            break
        case _:
            print('Input tidak valid')
    