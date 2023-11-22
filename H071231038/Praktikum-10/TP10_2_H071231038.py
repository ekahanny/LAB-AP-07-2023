class Gun:
    def __init__(self,model,caliber):
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
    

class Pistol(Gun):
    def __init__(self, model, caliber):
        super().__init__(model, caliber)

class AssaultRiffle(Gun):
    def __init__(self, model, caliber):
        super().__init__(model, caliber)
        self.burstmode = False
    
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
    
class SubMachineGun(Gun):
    def __init__(self, model, caliber):
        super().__init__(model, caliber)
        self.silencer = False
    
    def action(self):
        while True:
            print("Press A to shoot")
            print("Press R to reload")
            print("Press G to unequip")
            print("Press B to see details")
            print("Press E to attach silencer")
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
            elif act == "E" or act == "e":
                if not self.silencer:
                    print("Silencer Attached")
                    self.silencer = True
                else:
                    print("Silencer Detached")
                    self.silencer = False
            elif act == "g" or act == "G":
                break

class SniperRifle(Gun):
    def __init__(self, model, caliber):
        super().__init__(model, caliber)
        self.scope = False
    
    def action(self):
        while True:
            print("Press A to shoot")
            print("Press R to reload")
            print("Press G to unequip")
            print("Press B to see details")
            print("Press Q to use scope")
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
            elif act == "Q" or act == "q":
                if not self.scope:
                    print("Scope ON")
                    self.scope = True
                else:
                    print("Scope OFF")
                    self.scope = False
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

gun3 = SubMachineGun("MAC-10",".45 ACP")
gun3.ammocap = 30
gun3.ammo = gun3.ammocap
gun3._firerate = 1090

gun4 = SniperRifle("M107A1",".50 BMG")
gun4.ammocap = 10
gun4.ammo = gun4.ammocap
gun4._firerate = 10

while True:
    print("Choose:")
    print(f"1.{gun1.model}\n2.{gun2.model}\n3.{gun3.model}\n4.{gun4.model}")
    x = int(input("-> "))
    if x == 1:
        gun1.action()
    elif x == 2:
        gun2.action()
    elif x == 3:
        gun3.action()
    elif x == 4:
        gun4.action()    
    break

        