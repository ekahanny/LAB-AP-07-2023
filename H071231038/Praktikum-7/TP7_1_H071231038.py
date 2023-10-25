import datetime
import random
import os


def intro():
    print("="*50)
    judul = "SELAMAT DATANG"
    print(judul.center(50))
    return("="*50)

print(intro())
nama_input = input("Masukkan nama kasir : ")

def inisial(nama):
    awal = nama_input[0]
    tengah = nama_input[len(nama_input)//2]
    akhir = nama_input[-1]
    return((awal+tengah+akhir).upper())

def id(nama):
    tanggal = datetime.datetime.now()
    waktu = datetime.datetime.now()
    id = f"{inisial(nama)}{tanggal.strftime('%y%m%d')}{waktu.strftime('%H%M')}{random.randint(100,1000)}"
    return id

def cari_transaksi(input_id):
    daftar_file = os.listdir("Invoices")
    for file in daftar_file:
        if file.startswith(input_id):
            with open(os.path.join("Invoices",file),"r") as file_invoice:
                isi = file_invoice.read()
            print(isi)
            return
    print("ID tidak ditemukan".center(50))
                          
while True:
    print("="*50)
    print("Pilih opsi:\n1. Transaksi Baru\n2. Cari Transaksi\n3. Keluar")
    print("="*50)
    input_opsi = int(input("Masukkan opsi pilihan: "))
    print("="*50)
    
    produk = []
    total_harga = 0
    waktu_transaksi = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
    isi_trx = []


    match input_opsi:
        case 1:
            while True:
                nama_produk = input("Masukkan nama produk   : ")
                harga = int(input("Masukkan harga produk  : "))
                jumlah = int(input("Masukkan jumlah produk : "))
                total = jumlah*harga
                total_harga += total
                produk.append([nama_produk,harga,jumlah,total])

                yt = str(input("Tambah produk? (Y/T)   : "))
                if yt.lower() == "y":
                    print("="*50)
                    continue
                elif yt.lower() == "t":
                    print("="*50)
                    print("TRANSAKSI BERHASIL".center(50))

                    garis = ("="*72)
                    garis2 = ("="*56)

                    if not os.path.exists("invoices"):
                        os.mkdir("Invoices")

                    nama_file = f"Invoices/{id(nama_input)}.txt"
                    with open(nama_file,"w") as file: 

                        nama_toko = f"TOKO {nama_input.upper()}"
                        struk1 = f" {nama_toko.center(69)}\n\n{garis}\nNama kasir         : {nama_input}\nWaktu transaksi    : {waktu_transaksi}\n{garis}\n\n"
                        file.write(struk1)
                        file.write("")

                        dp = "Daftar Produk".center(56)
                        file.write("\t"+dp+"\n")
                        file.write(f"\t{garis2}\n")
                        tabel1 = f"\t|{'Nama'.center(17)}|{'Harga'.center(12)}|{'Jumlah'.center(9)}|{'Total'.center(13)}|"
                        file.write(f"{tabel1}\n")
                        file.write(f"\t{garis2}\n")
                        for nama, harga, jumlah, total in produk:
                            if len(nama)>14:
                                nama = nama[0:14] + ".."
                            file.write(f"\t|{str(nama).center(17)}|{('Rp'+str(harga)).center(12)}|{str(jumlah).center(9)}|{('Rp'+str(total)).center(13)}|\n")
                        file.write(f"\t{garis2}\n")
                        file.write(f"\t|{'Total'.center(30)}|{('Rp'+str(total_harga)).rjust(23)}|\n")
                        file.write(f"\t{garis2}\n")
                        file.write("\n")
                        file.write(f"{garis}\n{'TERIMA KASIH TELAH BERBELANJA'.center(69)}\n{garis}\n")  
                    
                    if not os.path.exists("trx_history.txt"):
                        with open ("trx_history.txt","w") as trx1:
                            trx1.write("="*62)
                            trx1.write("\n|"+("RIWAYAT TRANSAKSI".center(60))+"|\n")
                            trx1.write("="*62)
                            trx1.write("\n"+"|"+("Waktu".center(15))+"|"+("ID Transaksi".center(22))+"|"+("Nominal Transaksi".center(21))+"|\n")
                            trx1.write(("="*62)+"\n")

                        with open ("trx_history.txt","a") as trx1:
                            nama_file1 = nama_file[9:-4]
                            isi_trx.append([waktu_transaksi,nama_file1,total_harga])
                            for waktu,id_trx,nominal in isi_trx:
                                trx1.write(f"|{str(waktu).ljust(15)}|{str(id_trx).center(22)}|{('Rp'+str(nominal)).center(21)}|\n")
                                trx1.write("="*62+"\n")
                    else:
                        with open ("trx_history.txt","a") as trx2:
                            nama_file1 = nama_file[9:-4]
                            isi_trx.append([waktu_transaksi,nama_file1,total_harga])
                            for waktu,id_trx,nominal in isi_trx:
                                trx2.write(f"|{str(waktu).ljust(15)}|{str(id_trx).center(22)}|{('Rp'+str(nominal)).center(21)}|\n")
                                trx2.write("="*62+"\n")               
                    break
        case 2:
            input_id = input("Masukkan ID transaksi : ")
            print("")
            cari_transaksi(input_id)
            print("")
        case 3:
            print("SAMPAI JUMPA".center(50))
            print("="*50)
            break
