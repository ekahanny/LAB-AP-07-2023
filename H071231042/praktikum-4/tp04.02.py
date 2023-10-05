def palindrom(x):
    if x.lower() == x[:: -1].lower():
        print("palindrom")
    else:
        print("bukan palindrom")

palindrom("radar")
palindrom("step on no pets")

kata = input("masukkan kata : ")
palindrom(kata)