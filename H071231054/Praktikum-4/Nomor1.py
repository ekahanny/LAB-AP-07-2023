def stringPermutation(input_string):
    try:
        if not isinstance(input_string, str):
            raise TypeError("Input harus berupa string")
        
        if len(input_string) < 2:
            raise ValueError("Panjang string minimal 2 karakter")
        
        permutations = []
    
        
        for i in range(len(input_string)):
            input_string = input_string[-1] + input_string[:-1]
            permutations.append(input_string)
        
        result = " | ".join(permutations) + " |"
        print(result)
    
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

# Test Case 1
stringPermutation("Mobil")

# Test Case 2
stringPermutation("Ayam")

# Test Case 3: Input yang tidak valid (bukan string)
stringPermutation(123)
