from .hero import Hero
from effects.effect import Effect

class Archer(Hero):
    def __init__(self, name: str, health: int, strength: int) -> None:
        super().__init__(name, health, strength)
        self._arrows: int = 10  # У лучника есть стрелы
        self._ice_arrows: int = 3  # У лучника есть ледяные стрелы

    def attack(self, opponent: Hero) -> None:
        """Реализация атаки лучника."""
        if self.is_frozen():
            print(f"({self.__class__.__name__}) {self.name} пропускает ход из-за заморозки")
        else:
            if self._arrows > 0:
                damage: int = self._strength
                opponent.take_damage(damage)
                self._arrows -= 1
                print(f"({self.__class__.__name__}) {self.name} наносит урон {damage} противнику ({opponent.__class__.__name__}) {opponent.name} (Осталось стрел: {self._arrows})")
            else:
                print(f"({self.__class__.__name__}) {self.name} не может атаковать: закончились стрелы!")

    def use_ability(self, target: Hero) -> None:
        """Реализация специальной способности лучника."""
        if self._ice_arrows > 0:
            self._ice_arrows -= 1
            print(f"({self.__class__.__name__}) {self.name} использует способность 'Ледяная стрела' на {target.name}!")
            target.freeze()  # Замораживает противника на 1 ход
            target.take_damage(self._strength)  # Наносит урон противнику
            print(f"({self.__class__.__name__}) {self.name} наносит урон {self._strength} противнику ({target.__class__.__name__}) {target.name}")
        else:
            print(f"({self.__class__.__name__}) {self.name} не хватает ледяных стрел для использования способности!")

    def describe(self) -> str:
        """Описание лучника."""
        return f"Лучник {self.name} (Здоровье: {self.health}, Сила: {self.strength}, Стрелы: {self._arrows}, Ледяные стрелы: {self._ice_arrows})"