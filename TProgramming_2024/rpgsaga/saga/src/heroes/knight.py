from .hero import Hero

class Knight(Hero):
    def __init__(self, name: str, health: int, strength: int) -> None:
        super().__init__(name, health, strength)
        self._immune_to_freeze = True  # Рыцарь невосприимчив к заморозке

    def attack(self, opponent: Hero) -> None:
        """Реализация атаки рыцаря."""
        if self.is_frozen():
            print(f"({self.__class__.__name__}) {self.name} пропускает ход из-за заморозки")
        else:
            damage: int = self._strength
            opponent.take_damage(damage)
            print(f"({self.__class__.__name__}) {self.name} наносит урон {damage} противнику ({opponent.__class__.__name__}) {opponent.name}")

    def use_ability(self, target: Hero) -> None:
        """Реализация специальной способности рыцаря."""
        print(f"({self.__class__.__name__}) {self.name} использует способность 'Удар возмездия' на {target.name}!")
        target.take_damage(self._strength * 2)  # Пример: удар возмездия наносит двойной урон

    def describe(self) -> str:
        """Описание рыцаря."""
        return f"Рыцарь {self.name} (Здоровье: {self.health}, Сила: {self.strength}, Невосприимчив к заморозке: {self._immune_to_freeze})"