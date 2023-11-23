import re

user = input("Masukkan username: ")
pola_user = r"^[A-Za-z0-9]{5,20}$"
result = re.search(pola_user,user)

if  result:
    email = input("Masukkan email: ")
    pola_email = r"^[a-z]+(\d{2,})?@[a-z]+\.(com|co\.id)$"
    re_email = re.search(pola_email,email)
    if re_email:
        password = input("Masukkan password: ")
        pola_pass = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}$"
        re_pass = re.search(pola_pass,password)
        if re_pass:
            print(f"\nRegistrasi berhasil! Halo {user}!")
        else:
            print("Password tidak memenuhi syarat.Registrasi gagal")
    else:
        print("Email tidak vaild. Registrasi gagal")
else:
    print("Username tidak valid. Registrasi gagal")