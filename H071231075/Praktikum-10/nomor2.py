# Encapsulation
class Motor:
    def __init__(self,merek, mesin, silinder):
        self._merek = merek
        self._mesin = mesin
        self._silinder = silinder

    def get_merek(self):
        return self._merek
    
    def get_mesin(self):
        return self._mesin
    
    def get_silinder(self):
        return self._silinder
    
class Yamaha(Motor):
    def info(self):
        return f"Motor {self._merek} dengan mesin  {self._mesin} dan {self._silinder}" 

class Honda(Motor):
    def info(self):
        return f"Motor {self._merek} dengan mesin  {self._mesin} dan {self._silinder}"  

# polymorphism
def tampilkan_info(motor):
    print(motor.info())

motor_yamaha = Yamaha("HONDA", "150cc",4)
motor_honda = Honda("YAMAHA", "200cc", 3)

tampilkan_info(motor_yamaha)
tampilkan_info(motor_honda)
