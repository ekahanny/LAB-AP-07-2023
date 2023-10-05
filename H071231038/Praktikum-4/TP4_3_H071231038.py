def maxnumber(*args):
    angkaterbesar = args[0]
    for i in args:
        if i > angkaterbesar:
            angkaterbesar = i
    return angkaterbesar
print(maxnumber(-200,-100,-400,-50))