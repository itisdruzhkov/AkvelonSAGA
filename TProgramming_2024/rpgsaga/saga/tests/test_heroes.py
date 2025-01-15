import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from heroes.knight import Knight
from heroes.archer import Archer
from heroes.mage import Mage

def test_knight_attack() -> None:
    knight: Knight = Knight("Артур", 100, 10)
    opponent: Archer = Archer("Лавилас", 80, 8)
    knight.attack(opponent)
    assert opponent.health == 70  # 80 - 10 = 70

def test_knight_ability() -> None:
    knight: Knight = Knight("Артур", 100, 10)
    opponent: Mage = Mage("Геральт", 50, 5)
    knight.use_ability(opponent)
    assert opponent.health == 37  # 50 - (10 * 1.3) = 37

def test_archer_ice_arrows() -> None:
    archer: Archer = Archer("Лавилас", 80, 8)
    opponent: Knight = Knight("Артур", 100, 10)
    archer.use_ability(opponent)
    assert archer._ice_arrows_used == 1

def test_mage_charm() -> None:
    mage: Mage = Mage("Геральт", 50, 5)
    opponent: Knight = Knight("Артур", 100, 10)
    mage.use_ability(opponent)
    assert mage._charm_used

if __name__ == "__main__":
    test_knight_attack()
    test_knight_ability()
    test_archer_ice_arrows()
    test_mage_charm()
    print("All heroes tests passed!")