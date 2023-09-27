# menghasilkan jumlah suku fibonacci

fibonacci = int(input(""))
x = 0
y = 1

for f in range(fibonacci):
    print(x, end=" ")
    z = x + y
    y = x
    x = z
