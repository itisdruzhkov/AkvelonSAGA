import random
from typing import List
from .knight import Knight
from .archer import Archer
from .mage import Mage
from .hero import Hero

class HeroFactory:
    @staticmethod
    def create_hero(hero_type: str, name: str, health: int, strength: int) -> Hero:
        if hero_type == "Knight":
            return Knight(name, health, strength)
        elif hero_type == "Archer":
            return Archer(name, health, strength)
        elif hero_type == "Mage":
            return Mage(name, health, strength)
        else:
            raise ValueError("Unknown hero type")

    @staticmethod
    def create_random_heroes(num_players: int) -> List[Hero]:
        names: List[str] = ["Артур", "Эльдар", "Геральт", "Пётр", "Лавилас", "Гарри", "Дамблдор", "Аркадий"]
        heroes: List[Hero] = []
        for _ in range(num_players):
            name: str = random.choice(names)
            names.remove(name)
            health: int = random.randint(50, 100)
            strength: int = random.randint(5, 20)
            hero_type: str = random.choice(["Knight", "Archer", "Mage"])
            heroes.append(HeroFactory.create_hero(hero_type, name, health, strength))
        return heroes