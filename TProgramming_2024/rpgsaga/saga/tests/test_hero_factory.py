import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from heroes.hero_factory import HeroFactory
from heroes.knight import Knight
from heroes.archer import Archer
from heroes.mage import Mage
from heroes.hero import Hero

def test_create_knight() -> None:
    knight: Hero = HeroFactory.create_hero("Knight", "Артур", 100, 10)
    assert isinstance(knight, Knight)
    assert knight.name == "Артур"
    assert knight.health == 100
    assert knight.strength == 10

def test_create_archer() -> None:
    archer: Hero = HeroFactory.create_hero("Archer", "Лавилас", 80, 8)
    assert isinstance(archer, Archer)
    assert archer.name == "Лавилас"
    assert archer.health == 80
    assert archer.strength == 8

def test_create_mage() -> None:
    mage: Hero = HeroFactory.create_hero("Mage", "Геральт", 50, 5)
    assert isinstance(mage, Mage)
    assert mage.name == "Геральт"
    assert mage.health == 50
    assert mage.strength == 5

def test_create_random_heroes() -> None:
    heroes: list[Hero] = HeroFactory.create_random_heroes(3)
    assert len(heroes) == 3
    for hero in heroes:
        assert isinstance(hero, (Knight, Archer, Mage))

if __name__ == "__main__":
    test_create_knight()
    test_create_archer()
    test_create_mage()
    test_create_random_heroes()
    print("All hero factory tests passed!")