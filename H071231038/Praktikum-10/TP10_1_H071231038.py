import re
import os

class DataUser:
    def __init__(self):
        self.nama = ""
        self.email = ""
        self.password = ""

def detail_user(data):
    if data is None:
        print("Data saat ini kosong")
    else:
        print(f"{'-'*40}\nNama: {data.nama}\nEmail: {data.email}\nPassword: {data.password}\n{'-'*40}")

def ubah_nama(data):
    if data is None:
        print("Data saat ini kosong")
    else:
        namabaru = input("Silahkan input nama baru: ")
        data.nama = namabaru

def jumlah_data_file():
    namafile = input("Silahkan Masukkan Nama File: ")
    try:
        with open(namafile + ".txt","r") as f:
            file = f.read()
            hitungfile = file.count("Nama")
            print(f"{'-'*40}\nBerhasil\nJumlah Data Pada File: {hitungfile}\n{'-'*40}")
    except FileNotFoundError:
        print(f"{'-'*40}\nTidak terdapat file dengan nama {namafile}.txt")
        hitungfile = 0
        print(f"Jumlah Data Pada File: {hitungfile}\n{'-'*40}")

def save_data_file(data):
    if data is None:
        print("Data saat ini kosong")
    else:
        namafile = input("Silahkan Masukkan Nama File: ")
        teks = f"+{'='*60}\nData yang Tersimpan\n+{'='*60}\n"
        try:
            with open(namafile + ".txt", "r") as f:
                baca = f.read()
                if teks not in baca:
                    with open(namafile + ".txt", "a") as f:
                        f.write(teks)
        except FileNotFoundError:
            with open(namafile + ".txt", "a") as f:
                f.write(teks)

        with open(namafile+".txt","a") as f:
            f.write(f"|Nama       : {data.nama}\n|Email      : {data.email}\n|Password   : {data.password}\n")
            f.write(f"+{'='*60}\n")
            print("Berhasil")
            return None

def buat_data_baru():
    datauser = DataUser()
    datauser.nama = input("Masukkan nama: ")

    while True:
        datauser.email = input("Masukkan email: ")
        if not re.match("[a-z0-9._%+-]+@student\.unhas\.ac\.id$",datauser.email):
            print("email salah")
        else:
            break
            
    while True:
        datauser.password = input("Masukkan password: ")
        polapassword = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,20}$"
        re_pass = re.search(polapassword,datauser.password)

        if not len(datauser.password) >= 8 and len(datauser.password) < 20:
            print("Password harus memiliki panjang 8-20 karakter")
        elif not re_pass:
            print("Password yang anda masukkan terlalu lemah, gunakan minimal 1 huruf kapital, huruf kecil, dan angka")
        else:
            print("Berhasil")
            return datauser

data = None
while True:
    print("1. Detail Anda")
    print("2. Ubah Nama")
    print("3. Jumlah Data pada File")
    print("4. Save Data pada File")
    print("5. Buat Data Baru")
    print("6. Keluar")

    pilihan = int(input("Silahkan Pilih Opsi Anda: "))

    if pilihan == 1:
        detail_user(data)
    elif pilihan == 2:
        ubah_nama(data)
    elif pilihan == 3:
        jumlah_data_file()
    elif pilihan == 4:
        data = save_data_file(data)
    elif pilihan == 5:
        data = buat_data_baru()
    elif pilihan == 6:
        print("sampai jumpa")
        break
