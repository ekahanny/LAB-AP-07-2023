while True:
    golongan=input('Golongan = ')
    golongan=golongan.upper()
    golongan1=['R1','R2','R3','B2','B3','I3','P1']
    if golongan in golongan1:break                
    else:print('data tidak valid, silahkan coba lagi')
   
while True:
    daya=input('Daya = ')
    daya=float(daya)
   
    match golongan:
        case 'R1':
            R1_list=[900,1300,2200]
            if daya in R1_list:break
            else:print('data tidak valid, silahkan coba lagi')
        case 'R2':
            if daya>=3500 and daya<=5500:break
            else:print('data tidak valid, silahkan coba lagi')
        case 'R3':
            if daya>=6600:break
            else:print('data tidak valid, silahkan coba lagi')
        case 'B2':
            if daya>=6600 and daya<=200000:break
            else:print('data tidak valid, silahkan coba lagi')
        case 'B3':
            if daya>200000:break
            else:print('data tidak valid, silahkan coba lagi')
        case 'I3':
            if daya>=200000:break
            else:print('data tidak valid, silahkan coba lagi')
        case 'P1':
            if daya>=6600 and daya<=200000:break
            else:print('data tidak valid, silahkan coba lagi')

pemakaian=input('Pemakaian = ')
pemakaian=float(pemakaian)

match golongan:
        case 'R1':
            if daya==900:tarif=1352
            elif daya==1300 or daya==2200:tarif=1444.70
        case 'R2':
            tarif=1699.53
        case 'R3':
            tarif=1699.53
        case 'B2':
            tarif=1444.70
        case 'B3':
            tarif=1114.74
        case 'I3':
            tarif=1314.12
        case 'P1':
            tarif=1523.28

tagihan=tarif*pemakaian

print(f'Pemakaian = Jumlah tagihan anda sebesar : Rp, {tagihan:,.1f}'.format(tagihan).replace(',','x').replace('.',',').replace('x','.'))