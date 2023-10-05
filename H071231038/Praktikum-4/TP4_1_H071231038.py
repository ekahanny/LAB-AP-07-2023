def stringpermutation(a):
    result = []
    for i in range(len(a)):
        kata_slice = a[i:] + a[:i]
        result.append(kata_slice +" |")
    result.reverse()
    return " ".join(result)
try:
    print(stringpermutation("Mobil"))
except :
    print("input salah")
