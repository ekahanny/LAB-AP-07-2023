import locale
locale.setlocale(locale.LC_ALL, "id_ID")

gol = str(input("Golongan = "))
daya = int(input("Daya = "))
pem = int(input("Pemakaian = "))

match gol, daya:
    case "R1",900:
        tarif = 1352
        tag = pem*tarif
        tag_id = locale.currency(tag, grouping=True)
        print(f"Jumlah tagihan anda sebesar : {tag_id}")
    
    case "R1",1300:
        tarif = 1444.7
        tag = pem*tarif
        tag_id = locale.currency(tag, grouping=True)
        print(f"Jumlah tagihan anda sebesar : {tag_id}")
    
    case "R1", 2200:
        tarif = 1444.7
        tag = pem*tarif
        tag_id = locale.currency(tag, grouping=True)
        print(f"Jumlah tagihan anda sebesar : {tag_id}")
    
    case "R2", daya:
        tarif = 1699.53
        daya >= 3500 and daya <= 5500
        tag = pem*tarif
        tag_id = locale.currency(tag, grouping=True)
        print(f"Jumlah tagihan anda sebesar : {tag_id}")
            
    case "R3", daya:
        tarif = 1699.53
        daya >= 6600
        tag = pem*tarif
        tag_id = locale.currency(tag, grouping=True)
        print(f"Jumlah tagihan anda sebesar : {tag_id}")
        
    
    case "B2", daya:
        tarif = 1444.7
        daya >= 6600 and daya <= 200000
        tag = pem*tarif
        tag_id = locale.currency(tag, grouping=True)
        print(f"Jumlah tagihan anda sebesar : {tag_id}")        
    
    case "B3", daya:
        tarif = 1114.74
        daya > 200000
        tag = pem*tarif
        tag_id = locale.currency(tag, grouping=True)
        print(f"Jumlah tagihan anda sebesar : {tag_id}")
        
    
    case "I3", daya:
        tarif = 1314.12
        daya >= 200000
        tag = pem*tarif
        tag_id = locale.currency(tag, grouping=True)
        print(f"Jumlah tagihan anda sebesar : {tag_id}")
    
    case "P1", daya:
        tarif = 1523.28
        daya >= 6600 and daya <= 200000
        tag = pem*tarif
        tag_id = locale.currency(tag, grouping=True)
        print(f"Jumlah tagihan anda sebesar : {tag_id}")
        
    case _:
        print("Data tidak valid")