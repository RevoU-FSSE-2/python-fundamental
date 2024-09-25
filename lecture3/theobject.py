class Person:
    
    name: str
    age: int
    height: float
    is_student: bool
    aliases: list
    kaki = 4

    def __init__(self, * , name, age, height, is_student, aliases):
        self.name = name
        self.age = age
        self.height = height
        self.is_student = is_student
        self.aliases = aliases

person = Person(name="John", 
                age=25, 
                height=180.5, 
                is_student=True, 
                aliases=["tewel", "jons", "jojo"])


# inheratance

# parent class
class BaseVehicle4Wheels:
    engine_type: str
    color: str
    wheels = 4
    def __init__(self, * , engine_type, color):
        self.engine_type = engine_type
        self.color = color

    def move(self):
        # hanya bisa di panggil oleh class yang sudah di init / di construct
        print(f"{self.engine_type} is moving")
    
    @staticmethod
    def stop():
        # bisa di panggil tanpa harus di construct
        print("stop")
    
    @classmethod
    def build_red_vehicle(cls, * , engine_type):
        # bisa di panggil tanpa harus di construct
        # dan biasanya digunakan untuk membuat object baru dengan parameter yang sudah di set
        return cls(engine_type=engine_type, color="red")





    
class FamilyCar(BaseVehicle4Wheels):
    def __init__(self, * , engine_type, color):
        super().__init__(engine_type=engine_type, color=color)
    
    def move(self):
        # override
        print("Family car is moving")

class SportCar(BaseVehicle4Wheels):
    def __init__(self, * , engine_type, color):
        super().__init__(engine_type=engine_type, color=color)

class PickupTruck(BaseVehicle4Wheels):
    def __init__(self, * , engine_type, color):
        super().__init__(engine_type=engine_type, color=color)


honda_civic = FamilyCar(engine_type="electric", color="red")
lambo = SportCar(engine_type="v8", color="yellow")
ford_ranger = PickupTruck(engine_type="diesel", color="black")
    # static type hint
vehicles : list[BaseVehicle4Wheels] = [honda_civic, lambo, ford_ranger]

for vehicle in vehicles:        
    vehicle.move()
    vehicle.stop()

list_random = [26, 17, 31, 44, 54, 77, 11, 20]