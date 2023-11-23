from abc import ABC, abstractmethod

class Gun(ABC):
    @abstractmethod
    def action(self):
        pass

class Pistol(Gun):
    def __init__(self,model,caliber):
        self.model = model
        self.model = model
        self._caliber = caliber
        self.ammocap = 0
        self.ammo = self.ammocap
        self._firerate = 0
    
    def getcaliber(self):
        return self._caliber
    
    def getfirerate(self):
        return self._firerate
    def setfirerate(self,firerate):
        self._firerate += firerate

    def detail(self):
        return(f"{'-'*20}\nModel: {self.model}\nCaliber: {self.getcaliber()}\nAmmo Capacity: {self.ammocap}\nFire Rate: {self.getfirerate()}\n{'-'*20}")
    
    def action(self):
        while True:
            print("Press A to shoot")
            print("Press R to reload")
            print("Press G to unequip")
            print("Press B to see details")
            act = input("-> ")
            if act == "a" or act == "A":
                if self.ammo <= 0:
                    print("Ammo: 0")
                    print("Reload")
                else:
                    self.ammo -= 1
                    print(f"Ammo: {self.ammo}")
            elif act == "r" or act == "R":
                self.ammo = self.ammocap
                print(f"ammo: {self.ammocap}")
            elif act == "b" or act == "B":
                print(self.detail())
            elif act == "g" or act == "G":
                break

class AssaultRiffle(Gun):
    def __init__(self, model, caliber):
        self.model = model
        self.model = model
        self._caliber = caliber
        self.ammocap = 0
        self.ammo = self.ammocap
        self._firerate = 0
        self.burstmode = False

    def getcaliber(self):
        return self._caliber
    
    def getfirerate(self):
        return self._firerate
    def setfirerate(self,firerate):
        self._firerate += firerate

    def detail(self):
        return(f"{'-'*20}\nModel: {self.model}\nCaliber: {self.getcaliber()}\nAmmo Capacity: {self.ammocap}\nFire Rate: {self.getfirerate()}\n{'-'*20}")
    
    def action(self):
        while True:
            print("Press A to shoot")
            print("Press R to reload")
            print("Press G to unequip")
            print("Press B to see details")
            print("Press E to toggle Burst Mode")
            act = input("-> ")
            if act == "a" or act == "A":
                if self.ammo <= 0:
                    print("Ammo: 0")
                    print("Reload")
                else:
                    if self.burstmode:
                        self.ammo -= 2
                        print(f"Ammo: {self.ammo}")
                    else:
                        self.ammo -= 1
                        print(f"Ammo: {self.ammo}")
            elif act == "r" or act == "R":
                self.ammo = self.ammocap
                print(f"ammo: {self.ammocap}")
            elif act == "b" or act == "B":
                print(self.detail())
            elif act == "E" or act == "e":
                if  not self.burstmode:
                    print("Burst Mode ON")
                    self.setfirerate(1200)
                    self.burstmode = True
                else:
                    print("Burst Mode OFF")
                    self.setfirerate(-1200)
                    self.burstmode = False
            elif act == "g" or act == "G":
                break
            

gun1 = Pistol("Glock 17","9 mm")
gun1.ammocap = 17
gun1.ammo = gun1.ammocap
gun1._firerate = 600

gun2 = AssaultRiffle("AN-94","5.45x39 mm")
gun2.ammocap = 30
gun2.ammo = gun2.ammocap
gun2._firerate = 600

while True:
    print("Choose:")
    print(f"1.{gun1.model}\n2.{gun2.model}\n(Press X to Exit)")
    x = input("-> ")
    if x == "1":
        gun1.action()
    elif x == "2":
        gun2.action()
    elif x == "X" or x == "x":
        break
    else:
        print("Invalid input")
        