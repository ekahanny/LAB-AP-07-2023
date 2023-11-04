import re
baris = int(input())


ipv4 = r"([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])"
ipv6 = r"([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4}$)"
list_output = []

for _ in range(baris):
    st = input("")
    if re.match(ipv4,st):
        list_output.append("IPv4")
    elif re.match(ipv6,st):
        list_output.append("IPv6")
    else:
        list_output.append("bukan ip")

print("")

for hasil in list_output:
    print(hasil)