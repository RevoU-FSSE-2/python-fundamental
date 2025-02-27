class Person:
    name: str
    age: int
    height: float
    is_student: bool
    aliases: list
    kaki: int = 2

    def __init__(self, *, name, age, height, is_student, aliases):
        self.name = name
        self.age = age
        self.height = height
        self.is_student = is_student
        self.aliases = aliases

    def introduce(self):
        print(
            f"Hello, my name is {self.name}, I am {self.age} years old, and my height is {self.height} cm"
        )


john = Person(
    name="John",
    age=25,
    height=180.5,
    is_student=True,
    aliases=["tewel", "jons", "jojo"],
)
anne = Person(
    name="Anne",
    age=21,
    height=165.5,
    is_student=True,
    aliases=[],
)


# inheratance

# parent class
class BaseVehicle4Wheels:
    engine_type: str
    color: str
    wheels = 4
    top_speed = 100
    seat = 2

    def __init__(self, *, engine_type, color):
        self.engine_type = engine_type
        self.color = color

    def move(self):
        # hanya bisa di panggil oleh class yang sudah di init / di construct
        print(f"{self.engine_type} is moving")

    def calculate_top_speed(self):
        return self.top_speed / self.seat

    @staticmethod
    def stop():
        # bisa di panggil tanpa harus di construct
        print("stop")

    @classmethod
    def build_red_vehicle(cls, *, engine_type):
        # bisa di panggil tanpa harus di construct
        # dan biasanya digunakan untuk membuat object baru dengan parameter yang sudah di set
        return cls(engine_type=engine_type, color="red")


class FamilyCar(BaseVehicle4Wheels):
    seat = 4
    name = "family car"
    top_speed = 150

    def __init__(self, *, engine_type, color):
        super().__init__(engine_type=engine_type, color=color)
    
    def move(self):
        # overide
        print(f"{self.engine_type} is moving slowly with family")


class SportCar(BaseVehicle4Wheels):
    seat = 2
    name = "sport car"
    top_speed = 400

    def __init__(self, *, engine_type, color):
        super().__init__(engine_type=engine_type, color=color)


class PickupTruck(BaseVehicle4Wheels):
    seat = 2
    name = "pickup truck"
    top_speed = 120

    def __init__(self, *, engine_type, color):
        super().__init__(engine_type="4wheeldrive", color=color)


honda_civic = FamilyCar(engine_type="electric", color="red")
lambo = SportCar(engine_type="v8", color="yellow")
ford_ranger = PickupTruck(engine_type="diesel", color="black")
#     # static type hint
vehicles: list[BaseVehicle4Wheels] = [honda_civic, lambo, ford_ranger]

for vehicle in vehicles:
    # vehicle.move()
    # print(vehicle.calculate_top_speed())
    # vehicle.stop()
    print(vehicle,isinstance(vehicle, BaseVehicle4Wheels))
