import sys
import os

# Добавляем папку src в path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from game import Game
from heroes.hero_factory import HeroFactory
from heroes.hero import Hero
from heroes.knight import Knight
from heroes.archer import Archer
from heroes.mage import Mage

def test_create_random_heroes() -> None:
    heroes: list[Hero] = HeroFactory.create_random_heroes(3)
    
    # Проверяем что возвращается правильное количество героев
    assert len(heroes) == 3
    
    # Проверяем что каждый герой имеет правильный тип и корректные атрибуты
    for hero in heroes:
        assert isinstance(hero, (Knight, Archer, Mage))
        assert isinstance(hero.name, str) and hero.name  # Имя не пустое
        assert isinstance(hero.health, int) and hero.health > 0  # Здоровье положительное
        assert isinstance(hero.strength, int) and hero.strength > 0  # Сила положительная

def test_fight() -> None:
    knight: Hero = HeroFactory.create_hero("Knight", "Артур", 1, 10)
    archer: Hero = HeroFactory.create_hero("Archer", "Лавилас", 80, 8)
    game: Game = Game(2)
    game.players = [knight, archer]
    winner: Hero = game._fight(knight, archer)
    assert winner == archer

if __name__ == "__main__":
    test_create_random_heroes()
    test_fight()
    print("All game tests passed!")