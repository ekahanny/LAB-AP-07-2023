golongan = input("masukkan golongan: ")
daya = int(input("masukkan daya: "))
pemakaian = int(input("masukan pemakaian: "))

match golongan , daya:
    case "R1", 900:
        tagihan = pemakaian * 1352  

        print(f"Jumlah tagihan anda sebesar : Rp{tagihan:,.1f}".replace(',','x').replace('.',',').replace('x','.'))
        
    case "R1", 1300:
        tagihan = pemakaian * 1444.70

        print(f"Jumlah tagihan anda sebesar : Rp{tagihan:,.1f}".replace(',','x').replace('.',',').replace('x','.'))

    case "R1", 2200:
        tagihan = pemakaian * 1444.70

        print(f"Jumlah tagihan anda sebesar : Rp{tagihan:,.1f}".replace(',','x').replace('.',',').replace('x','.'))

    case "R2", daya:
        if daya >= 3500 and daya <= 5500:
            tagihan = pemakaian * 1699.53

            print(f"Jumlah tagihan anda sebesar : Rp{tagihan:,.1f}".replace(',','x').replace('.',',').replace('x','.'))
   
    case "R3", daya:
        if daya >= 6600:
            tagihan = pemakaian * 1699.53

            print(f"Jumlah tagihan anda sebesar : Rp{tagihan:,.1f}".replace(',','x').replace('.',',').replace('x','.'))

    case "B2", daya:
        if daya >= 6600 and daya <= 200000:
            tagihan = pemakaian * 1444.70

            print(f"Jumlah tagihan anda sebesar : Rp{tagihan:,.1f}".replace(',','x').replace('.',',').replace('x','.'))

    case "B3", daya:
        if daya > 200000:
            tagihan = pemakaian * 1114.74

            print(f"Jumlah tagihan anda sebesar : Rp{tagihan:,.1f}".replace(',','x').replace('.',',').replace('x','.'))

    case "I3", daya:
        if daya >= 200000:
            tagihan = pemakaian * 1314.12

            print(f"Jumlah tagihan anda sebesar : Rp{tagihan:,.1f}".replace(',','x').replace('.',',').replace('x','.'))

    case "P1", daya:
        if daya >= 6600 and daya <= 200000:
            tagihan = pemakaian * 1523.28

            print(f"Jumlah tagihan anda sebesar : Rp{tagihan:,.1f}".replace(',','x').replace('.',',').replace('x','.'))

    case _:
        print("Data tidak valid")
