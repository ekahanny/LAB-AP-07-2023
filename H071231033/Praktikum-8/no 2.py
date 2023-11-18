import re

patternIPv4 = (r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[01]?[0-9][0-9]?)$")
patternIPv6 = (r"^([A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}$")
banyak      = int(input("Ingin Berapa Kali Loop? : "))
List        = []

for i in range(banyak):
    i = input("Masukkan IP : ")
    List.append(i)
for ip in List:
    if re.search(patternIPv4, ip):
        print("IPv4")
    elif re.search(patternIPv6, ip):    
        print("IPv6")
    else:
        print("Bukan IP Address")
