from no1 import Warrior, Assassin, Support

warrior = Warrior("bambang", position=10)
assassin = Assassin("joko", position=25)
support = Support("udin", position=30)
# sebelum
print("health (before)", warrior.get_health())
print("Assassin menyerang warrior")
assassin.attack(warrior)
# sesudah
print("health (after) diserang assassin", warrior.get_health())
print("-"*10)
# sebelum
print("Warrior (health)", warrior.get_health())
print("Support (speed) default: ",support.get_speed())
print("support pake ulti ke warrior")
support.special(warrior)
# sesudah
print("Warrior (health)", warrior.get_health())
print("Support (speed): ",support.get_speed())

assassin.movement("R")
print("Posisi assassin sekarang adalah:", assassin.get_position())