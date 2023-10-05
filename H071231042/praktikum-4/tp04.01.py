def stringpermutation(kata):
    for i in range(len(kata)):
        kata = kata[-1] + kata[:-1]
        print (kata, end=" | ")
try:
    stringpermutation("mobil")
    print()
    stringpermutation("ayam")
    print()
    stringpermutation("123")

except TypeError :
    print(" error ketika dia bukan stringpermutation")

