class Human:
    def __init__(self,nama,posisi):
        self.nama = nama
        self.__posisi = posisi
        self._speed = 0
    
    def getposisi(self):
        return self.__posisi
    def setposisi(self,posisi):
        self.__posisi = posisi
    
    def getspeed(self):
        return self._speed
    def setspeed(self,speed):
        self._speed = speed

    def movement(self,arah):
        if arah == "L":
            self.__posisi -= self.getspeed()
        elif arah == "R":
            self.__posisi += self.getspeed()

class Hero(Human):
    def __init__(self,nama,posisi):
        super().__init__(nama,posisi)
        self._power = 15
        self._health = 400
        self._armor = 15
        self.setspeed(3)
    
        
    def getpower(self):
        return self._power
    def setpower(self,power):
        self._power = power

    def gethealth(self):
        return self._health
    def sethealth(self,health):
        self._health = health

    def getarmor(self):
        return self._armor
    def setarmor(self,armor):
        self._armor = armor

    def attack(self,target):
        target._health = target._health - self.getpower()

class Warrior(Hero):
    def __init__(self, nama, posisi):
        super().__init__(nama, posisi)
        self.setpower(26)
        self.setarmor(30)

    def special(self,target):
        self.setarmor(45)
        self.setpower(32)
        target._health = target._health - self.getpower()

class Assassin(Hero):
    def __init__(self, nama, posisi):
        super().__init__(nama, posisi)
        self.setpower(35)
        self.setspeed(4)

    def special(self,target):
        self.setarmor(42)
        self.setspeed(6)
        target._health = target._health - self.getpower()

class Support(Hero):
    def __init__(self, nama, posisi):
        super().__init__(nama, posisi)
        self.sethealth(500)
        self.setarmor(8)
        self.setspeed(4)
    def special(self,target):
        self.setspeed(6)
        target._health = target._health + 150
        

warrior1 = Warrior("bambang",10)
assassin1 = Assassin("joko",25)
support1 = Support("udin",30)


print("health (before)", warrior1.gethealth())
assassin1.attack(warrior1)

print("health (after)", warrior1.gethealth())
print("-"*20)

print("Warrior (health)", warrior1.gethealth())
print("Support (speed) : ",support1.getspeed())
support1.special(warrior1)
 
print("Warrior (health)", warrior1.gethealth())
print("Support (speed): ",support1.getspeed())

print(f"\n{'-'*20}\nposition before")
print (warrior1.getposisi())

print("position after")
warrior1.movement("R")
print(warrior1.getposisi())