def palindrom(word: str) -> str:
    # Menghilangkan spasi dan mengubah huruf menjadi huruf kecil
    cleaned_word = ''.join(filter(str.isalnum, word)).lower()
    
    # Memeriksa apakah kata sama dengan kata yang dibalik
    if cleaned_word == cleaned_word[::-1]:
        return "Palindrom"
    else:
        return "Bukan Palindrom"

# Test Case 1
result1 = palindrom("Radar")
print(result1)

# Test Case 2
result2 = palindrom("Step on no pets")
print(result2)
