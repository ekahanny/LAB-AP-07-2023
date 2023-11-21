from abc import ABC, abstractmethod

class Manusia(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def suara(self):
        pass

    def nama(self):
        return self.nama
    
class Faiz(Manusia):
    def suara(self):
        return "pinjam dulu seratus"
    
class Muslih(Manusia):
    def suara(self):
        return "wkwk"
    
f = Faiz("Faiz")
m = Muslih("Muslih")

print(f'{f.suara()}')
print(f'{m.suara()}')