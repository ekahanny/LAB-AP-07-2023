import re

username = input("Masukkan Username : ")
pola_usn = r"^[A-Za-z0-9]{5,20}"
if re.fullmatch(pola_usn, username):
    email       = input("Masukkan Email    : ")
    pola_email = r"^[a-z]+([0-9]{2,})?@([a-z]+)(\.com|\.co\.id)"
    if re.fullmatch(pola_email, email):
        password    = input("Masukkan Password : ")
        pola_pass  = r"[A-Za-z0-9]{8,}"
        if re.fullmatch(pola_pass, password):
            print(f"Registrasi Berhasil!, Selamat datang, {username}!")
        else:
            print("Password anda tidak valid")
    else:
        print("Email yang dimasukkan tidak valid!")
else:
    print("Username yang dimasukkan tidak valid!")


