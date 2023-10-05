# Menghitung BMI
print("Pilih Gender Anda")
print('1. Pria')
print('2. Wanita')
gender = int(input('= '))

TB = int(input("Masukkan tinggi badan (cm) : ")) / 100
BB = int(input("Masukkan berat badan (kg) : "))
a = BB / (TB**2)

if gender == 1:
    if a < 18 :
        b = (f"Anda Tergolong Underweight dengan BMI {a:.2f}")
        print(b)
    elif a >= 18 or a <=23.9:
        b = (f"Anda Tergolong Normal dengan BMI {a:.2f}")
        print(b)
    elif a >= 24 or a <= 26.9:
        b = (f"Anda Tergolong Overweight dengan BMI {a:.2f}")
        print(b)
    elif a >=27 :
        b = ("Anda Tergolong Obese dengan BMI {a:.2f}")
        print(b)

if gender == 2:
    if a < 17 :
        b = (f"Anda Tergolong Unerweight dengan BMI {a:.2f}")
        print(b)
    elif a >= 17 or a <= 23.9:
        b = (f"Anda Tergolong Normal dengan BMI {a:.2f}")
        print(b)
    elif a >= 24 or a <= 27.9:
        b = (f"Anda Tergolong Overweight dengn BMI {a:.2f}")
        print(b)
    elif a >= 28:
        b = (f"Anda Tergolong Obese dengn BMI {a:.2f}")
        print(b)

    
    
