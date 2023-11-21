import re
import os

class UserData:
    def __init__(self, nama="", email="", password=""):
        self.nama = nama
        self.email = email
        self.password = password

    def validate_email(self):
        pattern = r"^(?=.*[\d])[a-z]+(?:\d{1,})?@student.unhas.ac.id$"
        return re.match(pattern, self.email)

    def validate_password(self):
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,20}$"
        return re.match(pattern, self.password)

    def display_data(self):
        if not self.nama and not self.email and not self.password:
            print("="*75)
            print("Data Saat Ini Kosong")
        else:
            print("="*75)
            print(f"Data anda adalah\nNama     : {self.nama}\nEmail    : {self.email}\nPassword : {self.password}")
            
    def change_name(self):
        if not self.nama:
            print("="*75)
            print("Data Saat Ini Kosong")
        else:
            print("="*75)
            self.nama = input("Silahkan Input Nama Baru : ")

    def create_new_data(self):
        print("="*75)
        self.nama = input("Silahkan Masukkan Nama Anda     : ")

        while True:
            self.email = input("Silahkan Masukkan Email Anda    : ")
            if not self.validate_email():
                print("="*75)
                print("Email yang anda masukkan salah")
                print("="*75)
            else:
                break

        while True:
            self.password = input("Silahkan Masukkan Password Anda : ")
            if len(self.password) < 8 or len(self.password) > 20:
                print("="*75)
                print("Password Harus Memiliki Panjang 8-20")
                print("="*75)
            elif not self.validate_password():
                print("="*75)
                print("Password Yang anda masukkan terlalu lemah")
                print("Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka")
                print("="*75)
            else:
                break

    def save_data_to_file(self):
        if not self.nama and not self.email and not self.password:
            print("="*75)
            print("Data Saat Ini Kosong")
        else:
            print("="*75)
            filename = input("Silahkan Masukkan Nama File : ")

            if not filename.endswith(".txt"):
                filename += ".txt"

            if os.path.exists(filename):
                with open(filename, "a") as file:
                    file.write(f'''|Nama     : {self.nama}
|Email    : {self.email}
|Password : {self.password}
+{"="*75}
''')
            else:
                with open(filename, "w") as file:
                    file.write(f'''+{"="*75}
|Data yang Tersimpan
+{"="*75}                              
|Nama          : {self.nama}
|Email         : {self.email}
|Password      : {self.password}
+{"="*75}
''')

            print("Berhasil")

            # Reset data
            self.nama = ""
            self.email = ""
            self.password = ""

user_data = UserData()

while True:
        print("="*75)
        print("Selamat Datang Silahkan Pilih Opsi Menu Anda")
        print("1. Detail Anda")
        print("2. Ubah Nama")
        print("3. Jumlah Data pada File")
        print("4. Save Data pada File")
        print("5. Buat Data Baru")
        print("6. Keluar")

        pilihan = input("Silahkan Pilih Opsi Anda : ")

        if pilihan == "1":
            user_data.display_data()

        elif pilihan == "2":
            user_data.change_name()

        elif pilihan == "3":
            print("="*75)
            filename = input("Silahkan Masukkan Nama File : ")

            if not filename.endswith(".txt"):
                filename += ".txt"

            if os.path.exists(filename):
                with open(filename, "r") as file:
                    lines = len(file.readlines())
                    panjang = (lines - 3)//4
                    print("Berhasil")
                    print(f"Jumlah Data Pada File : {panjang} Data")
            else:
                print(f"Tidak Terdapat File dengan nama {filename}")
                print("Jumlah Data Pada File : 0 Data")

        elif pilihan == "4":
            user_data.save_data_to_file()

        elif pilihan == "5":
            user_data.create_new_data()

        elif pilihan == "6":
            print("="*75)
            print("Sampai Jumpa Lagi")
            break

        else:
            print("Silahkan pilih opsi 1-6!")