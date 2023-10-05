x= int(input("input = "))
a = 0
b = 1
for i in range(x):
    print(a,end="")
    total = a + b
    a = b
    b = total
