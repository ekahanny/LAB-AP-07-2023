while True:
    try:
        derajat = float(input(""))
        totaldetik = int(derajat * 240 + 21600)%86400
        jam = totaldetik // 3600
        menit = (totaldetik % 3600) // 60
        detik = totaldetik & 60

        if 6 <= jam < 12:
            print("selamat pagi")
        elif 12 <= jam < 15:
            print("selamat siang")
        elif 15 <= jam < 18:
            print("selamat sore")
        else:
            print("selamat malam")

        print(f"{jam:02}:{menit:02}:{detik:02}")
    except:
        print("End of file")
        break