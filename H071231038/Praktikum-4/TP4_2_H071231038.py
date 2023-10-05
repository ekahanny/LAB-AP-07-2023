def palindrom(a : str) -> str:
    a = a.lower()
    if a == a[::-1]:
        return "Palindrom"
    else:
        return "Bukan Palindrom"
    
hasil = palindrom("aku")
print(hasil)
