x1 = list(map(int, (input("masukan array ke-1 :").split())))
x2 = list(map(int, (input("masukan array ke-2 :").split())))
# map untuk mengelompokan 
# tipe data list diubah menjadi tipe data set agar  fungsi intersection dapat digunakan

x1=set(x1)
x2=set(x2)
x = x1.intersection(x2)
var = tuple(x)
# outputnya diminta tuple
p = len(var)
if p > 0 :
    print(f"terdapat {p} buah duplikat yaitu {var}")
else:
    print(f"tidak ada duplikasi ditemukan")