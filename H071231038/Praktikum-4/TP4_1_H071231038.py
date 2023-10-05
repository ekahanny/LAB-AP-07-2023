def stringpermutation(a):
    try:
        result = []
        for i in range(len(a)):
            kata_slice = a[i:] + a[:i]
            result.append(kata_slice +" |")
            result.reverse()
        return " ".join(result)
    except :
        print("input salah")

print(stringpermutation("Ayam"))
