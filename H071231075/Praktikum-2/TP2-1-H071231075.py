print("pilih gender anda")
print("1.pria")
print("2.wanita")
while True:
     golongan=input('= ')
     golongan=int(golongan)
     golongan1=[1,2]
     if golongan in golongan1 :break
     else:print('hanya boleh antara 1 atau 2')
tinggi_badan =float (input("masukkan tinggi badan : "))
berat_badan =float(input("masukkan berat badan :" ))

BMI = berat_badan  / ((tinggi_badan/100)**2)
if golongan==1:
     if BMI <18:
         print('anda tergolong Underweight dengan BMI',format(BMI,'.2f'))
     elif 18 <= BMI < 23.9:
         print('anda tergolong Normal dengan BMI',format(BMI,'.2f'))
     elif 24 <= BMI < 26.9:
          print('anda tergolong Overweight dengan BMI', format(BMI,'.2f'))  
     elif  BMI >=27:
          print ('anda tergolong Obese dengan BMI', format(BMI,'.2f'))
     else:
        print("error")

if golongan==2: 
     if BMI <17:
          print('anda tergolong Underweight dengan BMI',format(BMI,'.2f'))
     elif BMI < 23.9:
          print('anda tergolong normal dengan BMI',format(BMI,'.2f'))
     elif BMI < 27.9:
          print('anda tergolong Overweight dengan BMI',format(BMI,'.2f'))
     elif BMI >=28:
          print('anda tergolong Obese dengan BMI',format(BMI,'.2f')) 
     else:
          print("error")         