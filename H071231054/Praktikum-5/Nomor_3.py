def anagram(kata1, kata2):
    if len(kata1) != len(kata2):
        return False
    for x in kata1:
        if kata1.count(x) != kata2.count(x):
            return False
    return True

if anagram(input("Masukkan kata pertama: ").replace(" ", "").lower(), input("Masukkan kata kedua: ").replace(" ", "").lower()): 
    print("True")
else:
   print("False")