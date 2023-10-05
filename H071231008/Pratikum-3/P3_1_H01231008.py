N = int(input("Fibonaci : "))
if N == 0:
    N = 1
a,b = 0, 1
for _ in range(N):
    print (a, end=" ")
    b,a = a, a+b