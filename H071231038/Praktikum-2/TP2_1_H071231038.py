Pria = "1"
Wanita = "2"
gender = ["1","2"]
print("Pilih Gender Anda\n1. Pria\n2. Wanita")

num = (input("= "))
while num not in gender:
    print("Invalid Input")
    print("Pilih Gender Anda\n1. Pria\n2. Wanita")
    num = (input("= "))

tinggi = int(input("Masukkan tinggi badan (cm) : "))
tinggi_m = tinggi / 100
berat = int(input("Masukkan berat badan (kg) : "))

bmi = berat / (tinggi_m**2)

if num == "1":
    if bmi >= 27:
        print(f"Anda tergolong obese dengan BMI {bmi:.2f}")
    elif bmi >= 24 and bmi < 27:
        print(f"Anda tergolong overweight dengan BMI {bmi:.2f}")
    elif bmi >= 18 and bmi < 24:
        print(f"Anda tergolong normal dengan BMI {bmi:.2f}")
    elif bmi < 18:
        print(f"Anda tergolong underweight dengan BMI {bmi:.2f}")


if num == "2":
    if bmi >= 28:
        print(f"Anda tergolong obese dengan BMI {bmi:.2f}")
    elif bmi >= 24 and bmi < 28:
        print(f"Anda tergolong overweight dengan BMI {bmi:.2f}")
    elif bmi >= 17 and bmi < 24:
        print(f"Anda tergolong normal dengan BMI {bmi:.2f}")
    elif bmi < 17:
        print(f"Anda tergolong underweight dengan BMI {bmi:.2f}")


