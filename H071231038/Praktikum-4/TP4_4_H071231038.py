def catandmouse(catA: int, catB: int, mosC: int) -> str:
    jarakAC = catA - mosC
    if catA < mosC:
        jarakAC = mosC - catA

    jarakBC = catB - mosC
    if catB < mosC:
        jarakBC = mosC - catB

    if jarakAC < jarakBC:
        return "cat A"
    elif jarakBC < jarakAC:
        return "cat B"
    else:
        return "mouse C"

hasil = catandmouse(catA=16, catB=24, mosC=15)
print(hasil)