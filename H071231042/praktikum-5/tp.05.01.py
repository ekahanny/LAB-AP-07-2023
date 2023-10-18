# x = input("kata pertama:")
# x2 = input("kata kedua :")
x = "Abc"
x2 = "Xyz"
x3= "".join(reversed(x2))
var = ""
for i in range(len(x)):
    var = var + x[i] + x3[i]

print(f"kata kata :{var}")