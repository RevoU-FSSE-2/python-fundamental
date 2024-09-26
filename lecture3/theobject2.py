class Laser:
    def __init__(self, laser_lenght):
        # CM
        self.laser_lenght = laser_lenght
    
    # @classmethod
    # def build_from_meter(Laser, laser_lenght):
    #     return Laser(laser_lenght * 100)
    
    @classmethod
    def build_from_meter(cls, laser_lenght):
        return cls(laser_lenght * 100)
    
    @staticmethod
    def conver_cm_to_meter(laser_lenght):
        return laser_lenght / 100
    
    def laser_lenght_meter(self):
        return self.conver_cm_to_meter(self.laser_lenght)
    
    def __str__(self):
        return f"Laser with lenght {self.laser_lenght} CM"

laser_cm = Laser(100)
laser_m = Laser.build_from_meter(1)
laser_long_range = Laser.build_from_meter(10)

# def conver_cm_to_meter(laser_lenght):
#     ...
# static
Laser.conver_cm_to_meter(2356436)
# instance method
# Laser(100).laser_lenght_meter()
# class method
# Laser.build_from_meter(1) -> Laser(100)