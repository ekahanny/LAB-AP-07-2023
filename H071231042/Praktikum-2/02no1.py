
print("pilih gender anda")
print("1.pria")
print("2.wanita")
gender = int(input("= "))
tinggi = float(input("masukan tinggi badan (cm): ")) / 100
berat = float(input("masukan berat badan (kg): "))
bmi = berat / tinggi**2

match gender:

    case 1:
        if bmi < 18:
            print(f"Anda tergolong Underweight dengan BMI {bmi:.2f}")
        elif 18 <= bmi < 24:
            print(f"Anda tergolong Normal dengan BMI {bmi:.2f}")
        elif 24 <= bmi < 27:
            print(f"Anda tergolong Overweight dengan BMI {bmi:.2f}")
        elif bmi >= 27:
            print(f"Anda tergolong Obese dengan BMI {bmi:.2f}")
        else:
            print("input tidak valid")
    case 2:
        if bmi < 17:
            print(f"Anda tergolong Underweight dengan BMI {bmi:.2f}")
        elif 17 <= bmi < 24:
            print(f"Anda tergolong Normal dengan BMI {bmi:.2f}")
        elif 24 <= bmi < 28:
            print(f"Anda tergolong Overweight dengan BMI {bmi:.2f}")
        elif bmi >= 28:
            print(f"Anda tergolong Obese dengan BMI {bmi:.2f}")
        else:
            print("Input tidak valid")