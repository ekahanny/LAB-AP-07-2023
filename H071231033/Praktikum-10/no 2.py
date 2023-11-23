from abc import ABC, abstractmethod

class AirMinum(ABC):
    def __init__(self, volume):
        self.__volume = volume  # Volume dalam mililiter

    @abstractmethod
    def deskripsi(self):
        pass

    def get_volume(self):
        return self.__volume

class LeMinerale(AirMinum):
    def deskripsi(self):
        return f"Le Minerale, Volume: {self.get_volume()}ml"

class Aqua(AirMinum):
    def deskripsi(self):
        return f"Aqua, Volume: {self.get_volume()}ml"

class Cleo(AirMinum):
    def deskripsi(self):
        return f"Cleo, Volume: {self.get_volume()}ml"

class Club(AirMinum):
    def deskripsi(self):
        return f"Club, Volume: {self.get_volume()}ml"

# Menciptakan objek
le_minerale = LeMinerale(1500)
aqua = Aqua(500)
cleo = Cleo(330)
club = Club(600)

print(le_minerale.deskripsi())
print(aqua.deskripsi())
print(cleo.deskripsi())
print(club.deskripsi())