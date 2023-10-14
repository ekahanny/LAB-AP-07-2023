def kata_baru(kata):
    if len(kata) <= 3:
        return "masukkan minimal 3 huruf"
    return kata[0] + kata[len(kata) // 2] + kata[-1]

print("", kata_baru(input("Masukkan kata : ")))