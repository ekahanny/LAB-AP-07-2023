s1 = str(input("str1 = "))
s2 = str(input("str2 = "))

rs2 = s2[::-1]

result = ""
k = min(len(s1),len(s2))

for j in range(k):
    karakter1 = s1[j]
    karakter2 = rs2[j]
    mixed = karakter1 + karakter2
    result += mixed

result += s1[k:] + rs2[k:]    
print(result)