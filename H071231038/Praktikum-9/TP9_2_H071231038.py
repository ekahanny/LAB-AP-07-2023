class Mahasiswa:
    def __init__(self,nama):
        self.nama = nama
        self.nim = ""
        self.jurusan = ""
        self.ipk = 0

    
    def tampilkaninfo(self):
        return (f"{'-'*30}\nNama      : {self.nama}\nNIM       : {self.nim}\nJurusan   : {self.jurusan}\nipk       : {self.ipk}\n{'-'*30}")
    
    def hitungpredikat(self):
        if self.ipk >= 3.5:
            return "Cumlaude".center(50)
        elif self.ipk < 3.5 and self.ipk >= 3.0:
            return "Sangat Memuaskan".center(30)
        elif self.ipk < 3.0 and self.ipk >= 2.5:
            return "Memuaskan".center(30)
        elif self.ipk <2.5 and self.ipk >= 2.0:
            return "Cukup".center(30)
        else:
            return "Kurang".center(30)

mahasiswa1 = Mahasiswa("Ivan")
mahasiswa1.nim = "H071231038"
mahasiswa1.jurusan = "Sistem Informasi"
mahasiswa1.ipk = 3.2

print(mahasiswa1.tampilkaninfo())
print(mahasiswa1.hitungpredikat())