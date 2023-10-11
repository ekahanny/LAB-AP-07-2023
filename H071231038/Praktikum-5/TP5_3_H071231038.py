a = str(input("kata pertama = "))
b = str(input("kata kedua = "))

input1 = a.replace(" ","").lower()
input2 = b.replace(" ","").lower()

char1 = []
char2 = []

for i in input1:
    char1.append(i)

for j in input2:
    char2.append(j)

sortedchar1 = sorted(char1)
sortedchar2 = sorted(char2)

print(sortedchar1 == sortedchar2)
