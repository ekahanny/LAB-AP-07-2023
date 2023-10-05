def besar(x):
    terbesar = x[0]
    for i in x:
        if terbesar < i:
            terbesar = i
    return terbesar
x = [1,2,4,6,9,3,1,9,10]
print(besar(x))
x = [0,1,90,430,23,212,34]
print(besar(x))