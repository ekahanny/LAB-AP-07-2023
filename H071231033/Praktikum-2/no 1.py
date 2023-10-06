gender=int(input("Pilih gender anda\n1. Pria\n2. Wanita\n= "))

if gender != 1 and gender != 2:
    print("Pilih input yang valid")
else:
    tb = int(input("Masukkan tinggi badan (cm) : ")) / 100
    bb = int(input("Masukkan berat badan (kg) : "))
    bmi = bb / tb**2

    if gender == 1:
        if bmi < 18  :
            kategori = "Underweight"
        elif 18 <= bmi < 24 :
            kategori = "Normal"
        elif 24 <= bmi < 27 :
            kategori = "Overweight"
        else:
            kategori = "Obese"
    else:
        if bmi < 17  :
            kategori = "Underweight"
        elif 17 <= bmi < 24 :
            kategori = "Normal"
        elif 24 <= bmi < 28 :
            kategori = "Overweight"
        else:
            kategori = "Obese"

    print(f"Anda tergolong {kategori} dengan BMI {bmi:.2f}")