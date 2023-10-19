print("Selamat datang! Untuk memulai silahkan input data anda\n")

nama_input = input("Input nama: ")
umur_input = input("Input umur: ")
alamat_input = input("Input alamat: ")
print("")

dictt = {"Nama": nama_input,"Umur": umur_input,"Alamat": alamat_input}

sd = f"Selamat datang {dictt['Nama']}! Silahkan pilih opsi"

garis = "================================================"

print(garis)
print(sd)
print(garis)
a = ("1. Detail Anda\n2. Ubah Nama\n3. Ubah Umur\n4. Ubah Alamat\n5. Keluar")
print(a)
print(garis)

opsi_input = int(input("Input opsi: "))

while opsi_input:
    if opsi_input == 1:
        print(garis)
        print("Data Anda adalah")
        print(f"Nama: {dictt['Nama']}\nUmur: {dictt['Umur']}\nAlamat: {dictt['Alamat']}")
    elif opsi_input == 2:
        nama_baru = input("Silahkan input nama baru: ")
        dictt['Nama'] = nama_baru
        sd = f"selamat datang {dictt['Nama']}! Silahkan pilih opsi" 
        print("Data sukses diperbarui")
    elif opsi_input == 3:
        umur_baru = input("Silahkan input umur baru: ")
        dictt["Umur"] = umur_baru
        print("Data sukses diperbarui")
    elif opsi_input == 4:
        alamat_baru = input("Silahkan input alamat baru: ")
        dictt["Alamat"] = alamat_baru
        print("Data sukses diperbarui")
    elif opsi_input == 5:
        print(garis)
        print(f"Sampai jumpa {dictt['Nama']}!")
        break
    else:
        print("input salah\n")
        

    print(garis)
    print(sd)
    print(garis)
    print(a)
    print(garis)
    opsi_input = int(input("Input opsi: "))