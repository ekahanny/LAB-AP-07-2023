
a = int(input("a = "))
while a == 0:
    print("nilai a tidak boleh sama dengan nol")
    a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
D = b**2 - 4*a*c

x1 = (-b + (D**0.5)) / (2*a)
#x1_real = x1.real
print(f"x1 = {x1:.2f}")

x2 = (-b - (D**0.5)) / (2*a)
#x2_real = x2.real
print(f"x2 = {x2:.2f}")