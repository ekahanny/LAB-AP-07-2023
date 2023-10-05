def maxnumber(*args):
    angkaterbesar = args[0]
    for i in args:
        if i > angkaterbesar:
            angkaterbesar = i
    return angkaterbesar
print(maxnumber(100,200,300,250))