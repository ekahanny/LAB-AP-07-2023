def maksimum(*args):
    if not args:
        raise ValueError("Tidak ada angka dalam daftar")

    max_num = args[0]  # Inisialisasi max_num dengan elemen pertama

    for num in args:
        if num > max_num:
            max_num = num

    return max_num

# Test Case 1
result1 = maksimum(1, 2, 4, 6, 9, 3, 1, 9, 10)
print(result1)  # Output: 10

# Test Case 2
result2 = maksimum(0, 1, 90, 430, 23, 212, 34)
print(result2)  # Output: 430
