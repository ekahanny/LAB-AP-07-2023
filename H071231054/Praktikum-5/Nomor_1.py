def campur(s1, s2):
    s3 = ""
    for i in range(min(len(s1), len(s2))):
        s3 += s1[i] + s2[-(i+1)]
    return s3 

print("Hasil mixed =", campur(input("s1 = "), input("s2 = ")))