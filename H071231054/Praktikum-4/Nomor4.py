def catAndMouse(catA, catB, mosC):
    # Hitung jarak antara kucing A dan tikus
    distance_A_to_mouse = abs(catA - mosC)
    
    # Hitung jarak antara kucing B dan tikus
    distance_B_to_mouse = abs(catB - mosC)
    
    if distance_A_to_mouse < distance_B_to_mouse:
        return "Cat A"
    elif distance_B_to_mouse < distance_A_to_mouse:
        return "Cat B"
    else:
        return "Mouse C"

# Test Case 1
result1 = catAndMouse(catA=16, catB=24, mosC=15)
print(result1)  # Output: "Cat A"

# Test Case 2
result2 = catAndMouse(catA=20, catB=10, mosC=15)
print(result2)  # Output: "Mouse C"
  