input_1 = input("Input array ke-1: ").split()
input_2 = input("Input array ke-2: ").split()

set_input1 = set(input_1)
set_input2 = set(input_2)

irisan = set_input1&set_input2
a = len(set_input1&set_input2)
irisan_str = ', '.join(irisan)
b = f"Terdapat {a} duplikat yaitu ({irisan_str})"

if a == 0:
    print("Tidak ada duplikasi ditemukan")
else:
    print(b)
