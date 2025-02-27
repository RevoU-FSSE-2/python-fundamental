from abc import ABC, abstractmethod


class BaseAbstracCharacter(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

    @abstractmethod
    def move(self):
        pass


class BaseHero(BaseAbstracCharacter):
    base_attack = 10
    base_defense = 5
    base_move = 5
    base_health = 100

    def __init__(self, name):
        print("building a Character")
        self.name = name

        # logic

    def attack(self):
        print(f"{self.name} is attacking with {self.base_attack}")

    def defend(self, attack_point):
        print(f"{self.name} is defending with {self.base_defense}")
        self.base_health -= attack_point

    def move(self):
        print(f"{self.name} is moving")


class Hero(BaseHero):
    pass


class Monster(BaseHero):
    pass
    # self.base_attack = 5

    # def attack(self):
    #     print(f"{self.name} is dancing")
    # super().attack()


hero1 = Hero("Kamen Rider")
hero1.attack()
monster = Monster("Golem")
monster.attack()
