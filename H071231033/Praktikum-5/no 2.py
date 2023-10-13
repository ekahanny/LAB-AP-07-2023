def karakterbaru(kata):
    huruftengah = len(kata) // 2
    if len(kata) % 2 == 0: 
        karaktertengah = kata[huruftengah - 1] + kata[huruftengah]
    else:
        karaktertengah = kata[huruftengah]
    return kata[0] + karaktertengah + kata[-1]


kata = 'alpha'
print(karakterbaru(kata)) 


