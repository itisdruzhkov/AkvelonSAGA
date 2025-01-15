from .hero import Hero

class Mage(Hero):
    def __init__(self, name: str, health: int, strength: int) -> None:
        super().__init__(name, health, strength)
        self._mana: int = 100  # У мага есть мана

    def attack(self, opponent: Hero) -> None:
        """Реализация атаки мага."""
        if self.is_frozen():
            print(f"({self.__class__.__name__}) {self.name} пропускает ход из-за заморозки")
        else:
            damage: int = self._strength // 2  # Маг наносит меньше урона в ближнем бою
            opponent.take_damage(damage)
            print(f"({self.__class__.__name__}) {self.name} наносит урон {damage} противнику ({opponent.__class__.__name__}) {opponent.name}")

    def use_ability(self, target: Hero) -> None:
        """Реализация специальной способности мага."""
        if self._mana >= 20:
            self._mana -= 20
            print(f"({self.__class__.__name__}) {self.name} использует способность 'Огненный шарик' на {target.name}!")
            target.take_damage(self._strength * 3)  # Пример: огненный шар наносит тройной урон
        else:
            print(f"({self.__class__.__name__}) {self.name} не хватает маны для использования способности!")

    def describe(self) -> str:
        """Описание мага."""
        return f"Маг {self.name} (Здоровье: {self.health}, Сила: {self.strength}, Мана: {self._mana})"